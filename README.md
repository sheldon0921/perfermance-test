# 接口与性能测试工程

这个项目用于维护两类自动化测试资产：

1. Postman Collection，通过 Newman 执行接口测试，并在 Jenkins 中展示 Allure Report。
2. JMeter JMX 脚本，通过 JMeter 非 GUI 模式执行性能测试，并在 Jenkins 中展示 JMeter 原生 HTML Dashboard。

当前项目不再维护历史 Python/pytest 接口自动化代码。

## 目录结构

```text
.
├── PostmanScene/                 # Postman 导出的 collection
│   ├── BaiduDemo/
│   ├── CommunityGroupBuying/
│   ├── DirectStoreVersion/
│   ├── HaveStoreVersion/
│   └── NoStoreVersion/
├── script/
│   └── simulate/                 # JMeter 压测脚本
├── utils/
│   ├── CollectionApi.sh          # 执行 Newman collection，输出 JUnit XML
│   ├── runJmeter.sh              # 执行 JMeter，并直接生成 HTML Dashboard
│   ├── generateJmeterReport.sh   # 基于已有 JTL 重新生成 JMeter Dashboard
│   ├── generateAllureResults.sh  # 将 Newman/JMeter 结果转换为 Allure results
│   └── generateAllureReport.sh   # 生成 Allure HTML 报告
├── JenkinsfileForLocal           # 本地 Jenkins 推荐流水线
├── JenkinsfileForNewman          # 仅 Newman 的简化流水线
├── Jenkinsfile                   # JMeter 分布式压测流水线
├── package.json
└── README.md
```

## 环境准备

本地需要：

```bash
brew install jmeter
npm install
```

如果要使用本地 Jenkins：

```bash
brew install jenkins-lts
brew services start jenkins-lts
```

Jenkins 默认地址：

```text
http://localhost:8080
```

首次解锁密码通常在：

```bash
cat ~/.jenkins/secrets/initialAdminPassword
```

## 本地执行 Postman/Newman

执行全部 collection：

```bash
npm run postman
```

执行指定 collection 目录：

```bash
npm run postman:have-store
npm run postman:direct-store
npm run postman:no-store
npm run postman:community
npm run postman:baidu
```

也可以直接传文件或目录：

```bash
bash utils/CollectionApi.sh PostmanScene/BaiduDemo/BaiduHome.json
bash utils/CollectionApi.sh PostmanScene/HaveStoreVersion
```

输出：

- `report/result/*.xml`：Newman JUnit XML，供 Jenkins JUnit 和 Allure 转换使用。

生成 Allure 报告：

```bash
npm run allure:report
```

输出：

- `report/allure-results/`
- `report/allure-report/index.html`

## 本地执行 JMeter

当前示例脚本：

```text
script/simulate/baidu_home.jmx
```

执行默认 JMeter 脚本：

```bash
npm run jmeter
```

执行指定 JMX：

```bash
bash utils/runJmeter.sh script/simulate/baidu_home.jmx
```

覆盖线程数、RampUp、持续时间：

```bash
env ThreadsCount=50 RampUp=10 time=120 npm run jmeter
```

输出：

- `report/jtlResult.jtl`：JMeter 原始结果。
- `report/report/index.html`：JMeter 原生 HTML Dashboard。

只基于已有 JTL 重新生成 Dashboard：

```bash
npm run jmeter:report
```

JMeter Dashboard 包含左侧导航栏、聚合统计、TPS/Throughput、响应时间、错误率、分位数、Over Time 等图表，是性能测试的主要报告入口。

## Jenkins 本地流水线

本地 Jenkins 推荐使用 `JenkinsfileForLocal`。它支持一个任务里通过参数选择接口测试或性能测试。

创建任务：

1. Jenkins 首页选择 `New Item`。
2. 输入任务名，例如 `perfermance-test-local`。
3. 类型选择 `Pipeline`。
4. `Pipeline` 可选择 `Pipeline script from SCM`，仓库指向本项目。
5. `Script Path` 填 `JenkinsfileForLocal`。

如果只是本机调试，也可以选择 `Pipeline script`，直接粘贴 `JenkinsfileForLocal` 内容。

### Jenkins 参数

| 参数 | 用途 | 默认值 |
| --- | --- | --- |
| `TEST_TYPE` | 选择执行 `postman` 或 `jmeter` | `postman` |
| `COLLECTION_PATH` | Postman collection 文件或目录，`TEST_TYPE=postman` 生效 | `PostmanScene/BaiduDemo/BaiduHome.json` |
| `CASE_FILE` | JMeter JMX 文件，`TEST_TYPE=jmeter` 生效 | `script/simulate/baidu_home.jmx` |
| `ThreadsCount` | JMeter 线程数 | `10` |
| `RampUp` | JMeter RampUp 秒数 | `10` |
| `time` | JMeter 持续时间，单位秒 | `60` |

### Jenkins 报告入口

Postman/Newman 构建：

- `Allure Report`：接口测试主报告。
- Jenkins JUnit 趋势：基于 `report/result/*.xml`。

JMeter 构建：

- `JMeter Dashboard`：性能测试主报告，包含聚合报告、TPS、响应时间、错误率和图表。
- `Allure Report`：会保留基础结果视角，但性能分析以 JMeter Dashboard 为准。

已移除的入口：

- `Test Report`：之前的轻量汇总页，已不再发布，避免和 Allure/JMeter Dashboard 重复。

### Jenkins HTML 报告 CSP

Allure 和 JMeter Dashboard 都是带 CSS/JavaScript 的 HTML 报告。Jenkins 默认 CSP 可能阻止报告正常渲染。

本地 Jenkins 已通过以下初始化脚本放宽 HTML 报告 CSP：

```text
~/.jenkins/init.groovy.d/local-html-report-csp.groovy
```

如果换一台机器部署 Jenkins，需要同步该配置，或在 Jenkins 启动参数中设置 `hudson.model.DirectoryBrowserSupport.CSP`。

## 其他 Jenkinsfile

`JenkinsfileForNewman`：

- 只执行 Newman。
- 适合只需要 collection JUnit 报告的简化任务。

`Jenkinsfile`：

- 面向 JMeter 性能测试。
- 支持 `Exec_Server` 参数，用于 JMeter 分布式执行机。
- 会归档 `report/jtlResult.jtl` 和 `report/report/**`。

## 生成文件与清理

以下目录/文件是构建产物，已加入 `.gitignore`：

- `node_modules/`
- `report/result/`
- `report/report/`
- `report/newman/`
- `report/jenkins/`
- `report/allure-results/`
- `report/allure-report/`
- `report/*.jtl`
- `jmeter.log`

`JenkinsfileForLocal` 每次构建开始会清理旧报告，避免 Postman 和 JMeter 构建结果互相混入。

## 维护约定

- 新增接口测试时，优先在 Postman 中维护 collection，再导出到 `PostmanScene/`。
- 新增性能测试时，把 `.jmx` 放到 `script/simulate/` 或后续约定的生产脚本目录。
- JMeter 脚本里的线程数、RampUp、持续时间建议使用属性变量，方便 Jenkins 通过 `ThreadsCount`、`RampUp`、`time` 覆盖。
- 接口测试失败优先看 `Allure Report` 和 Jenkins JUnit 趋势。
- 性能测试分析优先看 `JMeter Dashboard`，不要用 Allure 判断 TPS/响应时间趋势。
