pipeline {
    agent any
    options {
    		buildDiscarder(logRotator(numToKeepStr: '25'))
    		timestamps()
            timeout(time:30, unit:"MINUTES")
    	}
    stages {
        stage('Prepare'){
            steps{
                echo '初始化执行环境：安装依赖包和工具'
                sh 'python3 -m pip install pipenv'
                sh 'python3 -m pipenv install --skip-lock'
                sh 'npm install'
                sh 'rm -rf report/result/*'
                sh 'cp report/categories.json report/result/'
            }
        }
        stage('Run Test Case') {
            failFast false
            steps {
            parallel(
                'Run Postman Case': {
                    nodejs('node10'){
                        echo '执行postman接口'
                        sh 'sh utils/CollectionApi.sh'
                    }
                },

                'Run Pytest Case': {
                    echo '执行py脚本中的复杂场景'
                    sh 'pipenv run pytest -v -n auto -capture=fd -m smoke --self-contained-html --reruns 2 -p no:warnings --alluredir report/result'
//                    sh 'pipenv run pytest -v -n auto -capture=fd -m smoke --self-contained-html --reruns 2 -p no:warnings --junit-xml=report/result/pytestout.xml'
                }
            )
            }
        }
    }
    post {
        always {
            junit allowEmptyResults: true, testResults: 'report/result/*.xml'
            allure includeProperties: false, jdk: '', results: [[path: 'report/result']]
        }
        failure {
            script {
                    currentBuild.description = "Failure"
                   }
            emailext(
                to:'wangliping@vchangyi.com,zhangxin@vchangyi.com,mujunqiang@vchangyi.com,xuetong@vchangyi.com,baizhe@vchangyi.com,wangjianmin@vchangyi.com,houyingcai@vchangyi.com,hanzhigang@vchangyi.com,yangqiao@vchangyi.com,zhaojie@vchangyi.com,zhujiaqi@vchangyi.com,huangxiaomin@vchangyi.com,maxiongwei@vchangyi.com,hulongyang@vchangyi.com,wangzhou@vchangyi.com,wanggenggeng@vchangyi.com',
//                 to:'mujunqiang@vchangyi.com,xuetong@vchangyi.com,baizhe@vchangyi.com',
                subject: '${JOB_NAME} 执行失败',
//                TODO 邮件需要跳转到 jenkins 工程的链接
                body: '${JOB_NAME} 报告：http://ci.tools.vchangyi.com/view/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B9%B3%E5%8F%B0/job/autotest/job/api-automated-testing/${BUILD_ID}/allure/\n<br>'+
                      '${JOB_NAME} 执行结果：http://ci.tools.vchangyi.com/view/%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95%E5%B9%B3%E5%8F%B0/job/autotest/job/api-automated-testing/${BUILD_ID}/testReport/\n<br>'
                      +'BUILD_URL：${BUILD_URL}\n<br>'
                      +'JOB_URL:${JOB_URL}\n<br>'
                )
        }
        success {
            script {
                   currentBuild.description = "Success"
           }
        }
        aborted {
            script {
                   currentBuild.description = "Aborted"
                  }
         }
    }
}
