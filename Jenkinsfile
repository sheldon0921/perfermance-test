#!/usr/bin/groovy
import groovy.transform.Field
import groovy.io.FileType

pipeline {
	agent {
	    node { label "main"}
	}
	options {
		buildDiscarder(logRotator(numToKeepStr: '150'))
		timestamps()
        timeout(time:1, unit:"HOURS")
	}
	parameters {
		string (
				defaultValue:'script/simulate/goods.jmx',
				description: '压测脚本，请将你的jmeter脚本push到远程仓库的script/目录下，压测环境的脚本放到simulate下，生产环境的放到production目录下',
				name : 'case_file')
		string (
        		        defaultValue: 'data/performanceData/spu_id.csv,data/performanceData/store_id.csv',
                    	description: '数据文件路径,有就填，没有就不填。多个数据文件使用[,]分割',
                    	name : 'dataFilePath'
                    	)
		string (
		        defaultValue: '100',
            	description: '线程数, 实际并发用户数=ThreadsCount * 启动的执行机数量，默认值100（即100*3（启动三台slave机器）=300并发）',
            	name : 'ThreadsCount'
            	)
        string (
               defaultValue: '300',
               description: '加压持续时间，单位：s, 默认值5min',
               name: 'time'
        )
        string (
                       defaultValue: '0',
                       description: '启动全部线程所需时间，单位：s, 默认值0',
                       name: 'RampUp'
        )
        string (
        		        defaultValue: '商品压测',
                    	description: '本次压测的场景描述',
                    	name : 'description'
                    	)
        extendedChoice (
                        defaultValue: '10.105.202.35,10.105.55.218,10.105.216.204',
                        description: '',
                        multiSelectDelimiter: ',',
                        name: 'Exec_Server',
                        quoteValue: false,
                        saveJSONParameterToFile: false,
                        type: 'PT_CHECKBOX',
                        value: '10.105.202.35,10.105.55.218,10.105.216.204',
                        visibleItemCount: 3
                        )
	}
	stages {
	    stage('GitSCM'){
	        steps {
	            git branch: 'performance',
	            credentialsId: 'f6cfb0c8-e1bb-4c43-97df-fba3b9eead67',
	            url: 'ssh://git@gitlab.chinawip.com:qa1/auto.git'
	        }
	    }
	    stage('Prepare') {
    			steps {
    				echo 'Delete the history report and Create an empty result file'
    				sh('rm -rf report/report/* && rm -rf report/jtlResult.jtl && touch report/jtlResult.jtl')
                    sh('sh utils/FixLogin.sh')
                    script {
                    def serverCount=Exec_Server.split(",").length
                    wrap([$class: 'BuildUser']) { BUILD_USER = env.BUILD_USER }
                    currentBuild.displayName = "#${BUILD_ID}-${BUILD_USER}"
                    currentBuild.description = "脚本路径:${case_file}\n线 程 数:${ThreadsCount}*${serverCount}\n持续时间:${time}秒(s)\n场景描述:${description}"
//                    sh("python3 utils/generateUserToken/getUserCookie.py")
//                    if (case_file.indexOf("production")!=-1 & case_file.indexOf("baOu")==-1){
//                                sh("rm -rf ${dataFilePath}")
//                  因为用到python的第三方库发送http请求获取用户token，所以先安装用到的python第三方库aiohttp
//                                sh("python3 -m pip install aiohttp")
//                  如果jmx路径中包含production则表示压测线上，需要先生成用户token
//                                print('压测数据准备中 ... ')
//                                sh("python3 utils/generateUserToken/getToken.py")
// ES user压测专有Shell脚本,根据传入的数据文件路径动态修改压测脚本（jmx）所引用的数据文件名称
                    if(case_file.indexOf("ESUser")!=-1){
                                sh("sh utils/fixScript.sh")
                    }
                  }
               }
    	    }
		stage('Performance Testing') {
			steps {
			    echo 'Start the JMeter service for the child node'
                sh("sh utils/startSlave.sh")
				echo 'Performance testing...'
                script {
                    @Field String res=""
                    exe_server = Exec_Server.replace('"','')
                    String[] ipArr= exe_server.split(',')
                    ipArr.each { res+=(it+":1098,")}
                    cmd = String.format(' -n -t file -R %s -l report/jtlResult.jtl', res).replace("file", case_file).replace(", -l"," -l")
                    sh("utils/jmeter/bin/jmeter -GThreadsCount="+ThreadsCount+" -GRampUp="+RampUp+" -Gtime="+time+cmd)
                }
			}
		}
		stage('Generate Report') {
        	steps {
        	        script {
//        	        为了让报告的样式显示出来这句话是必须的。得一直留着，否则Jenkins机器重启之后Jenkins报告样式+数据就丢了
        	            System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")
        	            sh('utils/jmeter/bin/jmeter -g report/jtlResult.jtl -e -o report/report')
        	        }
        		  }
      }
	}
	post {
            always {
                	publishHTML([allowMissing: false,
                				alwaysLinkToLastBuild: true,
                				keepAll: true,
                        		reportDir: 'report/report/',
                				reportFiles: 'index.html',
                				reportName: 'Apache JMeter Test Report',
                				reportTitles: 'JMeter Report'])
//                  不管流水线执行结果如何都需要停止slave执行机，否则下次执行就会抛错，除非下次执行的时候slave执行机上的压测任务已经执行完了
                    sh('sh utils/stopSlave.sh')
            }
            success {
                script{
                       if(case_file.indexOf("production")!=-1){
                             emailext(
                                      to:'13020776968@163.com',
                                      subject: '${description}压测报告',
                                      body: '${description}压测报告：http://ci.tools.chinawip.com/view/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B9%B3%E5%8F%B0/job/autotest/job/performance-testing/${BUILD_ID}/Apache_20JMeter_20Test_20Report/\n<br>'+
                                            'BUILD_URL：${BUILD_URL}\n<br>'
                                            +'JOB_URL:${JOB_URL}\n<br>'
                                      )
                        }
                     }
            }
        }
}