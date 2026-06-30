#!/usr/bin/groovy

pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '150'))
        timestamps()
        timeout(time: 1, unit: "HOURS")
    }
    parameters {
        string(
            defaultValue: 'script/simulate/baidu_home.jmx',
            description: 'JMeter 脚本路径。压测环境放到 script/simulate，生产环境放到 script/production',
            name: 'case_file'
        )
        string(
            defaultValue: '',
            description: '数据文件路径，多个文件用英文逗号分隔；没有数据文件时可留空',
            name: 'dataFilePath'
        )
        string(
            defaultValue: '10',
            description: '线程数。实际并发用户数 = ThreadsCount * 执行机数量',
            name: 'ThreadsCount'
        )
        string(
            defaultValue: '60',
            description: '加压持续时间，单位秒',
            name: 'time'
        )
        string(
            defaultValue: '0',
            description: '启动全部线程所需时间，单位秒',
            name: 'RampUp'
        )
        string(
            defaultValue: '本地 JMeter 压测',
            description: '本次压测场景说明',
            name: 'description'
        )
        string(
            defaultValue: '',
            description: 'JMeter slave 执行机列表',
            name: 'Exec_Server'
        )
    }
    stages {
        stage('Prepare') {
            steps {
                sh 'bash utils/cleanReports.sh jmeter'
                script {
                    def serverCount = params.Exec_Server?.trim() ? params.Exec_Server.split(',').length : 1
                    currentBuild.displayName = "#${BUILD_ID}-${params.description}"
                    currentBuild.description = "脚本路径:${case_file}\n线程数:${ThreadsCount}*${serverCount}\n持续时间:${time}秒(s)\n场景描述:${description}"

                    if (fileExists('utils/FixLogin.sh')) {
                        sh 'sh utils/FixLogin.sh'
                    }
                    if (case_file.indexOf('ESUser') != -1 && fileExists('utils/fixScript.sh')) {
                        sh 'sh utils/fixScript.sh'
                    }
                }
            }
        }
        stage('Performance Testing') {
            steps {
                script {
                    def jmeterBin = fileExists('utils/jmeter/bin/jmeter') ? 'utils/jmeter/bin/jmeter' : 'jmeter'

                    if (fileExists('utils/startSlave.sh')) {
                        sh 'sh utils/startSlave.sh'
                    }

                    def remoteArgs = ''
                    if (params.Exec_Server?.trim()) {
                        def servers = params.Exec_Server.replace('"', '').split(',').collect { "${it.trim()}:1098" }.join(',')
                        remoteArgs = " -R ${servers}"
                    }

                    sh """
                        "${jmeterBin}" -n \
                          -t "${params.case_file}"${remoteArgs} \
                          -l report/jtlResult.jtl \
                          -JThreadsCount="${params.ThreadsCount}" \
                          -JRampUp="${params.RampUp}" \
                          -Jtime="${params.time}" \
                          -GThreadsCount="${params.ThreadsCount}" \
                          -GRampUp="${params.RampUp}" \
                          -Gtime="${params.time}"
                    """
                }
            }
        }
        stage('Generate Report') {
            steps {
                script {
                    def jmeterBin = fileExists('utils/jmeter/bin/jmeter') ? 'utils/jmeter/bin/jmeter' : 'jmeter'
                    sh "JMETER_BIN=\"${jmeterBin}\" bash utils/generateJmeterReport.sh"
                    sh 'TEST_TYPE=jmeter bash utils/buildReportIndex.sh'
                }
            }
        }
    }
    post {
        always {
            archiveArtifacts allowEmptyArchive: true, artifacts: 'report/jtlResult.jtl,report/report/**,report/jenkins/**'
            publishHTML target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'report/jenkins',
                reportFiles: 'index.html',
                reportName: 'Report Index'
            ]
            publishHTML target: [
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'report/report',
                reportFiles: 'index.html',
                reportName: 'JMeter Dashboard'
            ]
            script {
                if (fileExists('utils/stopSlave.sh')) {
                    sh 'sh utils/stopSlave.sh'
                }
            }
        }
    }
}
