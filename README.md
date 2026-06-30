# 接口与性能测试工程

这个项目用于维护两类自动化测试资产：

1. Postman Collection，通过 Newman 执行接口测试，并生成 JUnit、Newman HTML 和 Allure 报告。
2. JMeter JMX 脚本，通过 JMeter 非 GUI 模式执行性能测试，并生成 JMeter 原生 HTML Dashboard。

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
│   ├── generateAllureReport.sh   # 生成 Allure HTML 报告
│   ├── buildReportIndex.sh       # 生成本地轻量报告索引页
│   ├── cleanReports.sh           # 安全清理报告产物
│   ├── common.sh                 # Shell 脚本公共安全校验函数
│   ├── verifyStatic.sh           # 静态检查脚本语法和清理入口
│   └── verifyLocal.sh            # 一键本地验证接口、性能和报告链路
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
npm ci
```

一键验证本地接口测试、性能测试、Allure 报告和轻量报告索引：

```bash
npm run verify:local
```

只验证报告清理路径安全保护：

```bash
npm run verify:safety
```

只验证 Shell 语法和清理入口约束：

```bash
npm run verify:static
```

清理本地报告产物：

```bash
npm run clean:reports
```

默认会执行 Baidu Demo collection 和 `script/simulate/baidu_home.jmx`。如需覆盖默认用例：

```bash
env POSTMAN_COLLECTION=PostmanScene/BaiduDemo/BaiduHome.json JMETER_CASE_FILE=script/simulate/baidu_home.jmx npm run verify:local
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

- `report/result/*.xml`：Newman JUnit XML，供 Jenkins JUnit、Allure 转换和本地 HTML 汇总使用。

一键生成 Allure 报告和轻量报告索引页：

```bash
npm run report
```

输出：

- `report/allure-results/`
- `report/allure-report/index.html`
- `report/jenkins/index.html`
- `report/newman/*.html`：由 Newman JUnit XML 衍生的 collection 明细页。

默认按 `TEST_TYPE=local` 同时汇总 Newman 和 JMeter；如需只生成某一类报告，可直接使用对应脚本：

```bash
npm run report:postman
npm run report:jmeter
```

只重新生成轻量索引页时，也可以选择对应类型：

```bash
npm run report:index:postman
npm run report:index:jmeter
```

这些脚本仍支持通过 `TEST_TYPE` 覆盖默认汇总类型。
`TEST_TYPE` 只接受 `postman`、`jmeter`、`local` 或 `unknown`，拼写错误会直接失败。

生成 Allure 报告：

```bash
npm run allure:report
```

输出：

- `report/allure-results/`
- `report/allure-report/index.html`

生成轻量报告索引页：

```bash
npm run report:index
```

输出：

- `report/jenkins/index.html`
- `report/newman/*.html`：由 Newman JUnit XML 衍生的 collection 明细页。

索引页会自动链接已存在的 Allure 报告、Newman 明细页、JMeter Dashboard 和 JTL 原始结果。

## 本地执行 JMeter

当前示例脚本：

```text
script/simulate/baidu_home.jmx
```

默认本地参数是 `ThreadsCount=1`、`RampUp=1`、`time=10`、`ThinkTimeMs=1000`，请求目标是 `https://www.baidu.com/`，用于快速验证 JMeter 链路。

执行默认 JMeter 脚本：

```bash
npm run jmeter
```

执行指定 JMX：

```bash
bash utils/runJmeter.sh script/simulate/baidu_home.jmx
```

覆盖线程数、RampUp、持续时间和请求目标：

```bash
env ThreadsCount=50 RampUp=10 time=120 ThinkTimeMs=1000 TargetDomain=apis-test.60kongjian.com TargetPath=/mobile/home/index npm run jmeter
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
| `ThreadsCount` | JMeter 线程数 | `1` |
| `RampUp` | JMeter RampUp 秒数 | `1` |
| `time` | JMeter 持续时间，单位秒 | `10` |
| `ThinkTimeMs` | JMeter 请求间隔，单位毫秒 | `1000` |
| `TargetDomain` | JMeter 目标域名 | `www.baidu.com` |
| `TargetProtocol` | JMeter 协议 | `https` |
| `TargetPath` | JMeter 请求路径 | `/` |

### Jenkins 报告入口

`JenkinsfileForLocal` 会通过 HTML Publisher 在构建页展示报告入口，并同时归档为 Jenkins artifacts。需要先在 Jenkins 插件管理中安装 `HTML Publisher` 插件；没有该插件时，流水线会在 `publishHTML` 步骤失败。

- `report/jenkins/index.html`：轻量报告索引页。
- `report/allure-report/index.html`：Allure 报告。
- `report/newman/*.html`：由 Newman JUnit XML 衍生的 collection 明细页。
- `report/report/index.html`：JMeter Dashboard，仅 `TEST_TYPE=jmeter` 时生成。
- `report/result/*.xml`：JUnit XML，用于 Jenkins 测试趋势。

本地文件系统也会保留同样的 `report/` 输出，调试时可以直接打开 `report/jenkins/index.html` 进入 Allure、Newman 和 JMeter 报告。

如果只看到“上次成功的成品”，说明 Jenkins 已经归档报告，但没有在任务页直接渲染 HTML 报告入口。安装 HTML Publisher 并使用当前 Jenkinsfile 后，构建详情页会出现 `Report Index`、`Allure Report`，以及按类型出现的 `JMeter Dashboard` 链接。

### Jenkins HTML 报告 CSP

Allure 和 JMeter Dashboard 都是带 CSS/JavaScript 的 HTML 报告。通过 Jenkins artifacts 下载或从本地文件系统打开时不需要额外插件。通过 HTML Publisher 在 Jenkins 页面内直接渲染时，Jenkins 的默认 CSP 可能会限制部分样式或脚本。

如报告页样式或脚本显示异常，可能需要配置 `hudson.model.DirectoryBrowserSupport.CSP`。

## 其他 Jenkinsfile

`JenkinsfileForNewman`：

- 只执行 Newman，默认使用 `PostmanScene/BaiduDemo/BaiduHome.json`。
- 适合只需要接口测试的简化任务。
- 会生成并发布/归档 JUnit XML、Newman HTML、Allure 报告和轻量报告索引。

`Jenkinsfile`：

- 面向 JMeter 性能测试。
- 支持 `Exec_Server` 参数，用于 JMeter 分布式执行机。
- 会生成并发布/归档轻量报告索引、`report/jtlResult.jtl` 和 `report/report/**`。

## 依赖安全

项目使用 `npm ci` 和 `package-lock.json` 固定依赖版本。

`package.json` 中的 `overrides` 用于压住 Newman 依赖链里的安全修复版本。当前验证结果：

```bash
npm audit
```

结果应为 `found 0 vulnerabilities`。

Jenkins 日志中可能仍出现来自 Newman 官方依赖链的 deprecated 提示，例如 `har-validator@5.1.5` 和 `@faker-js/faker@5.5.3`。这些不是 `npm audit` 漏洞；不要为了消除提示强行覆盖 `postman-runtime` 大版本，已验证会导致 Newman 脚本执行异常。

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
- `report/*.html`
- `jmeter.log`

各 Jenkinsfile 每次构建开始会通过 `utils/cleanReports.sh` 清理对应旧报告，避免失败构建归档到上一次的旧索引或测试结果。

报告清理脚本只允许清理工作区相对路径，可通过 `npm run verify:safety` 回归验证。

`npm run verify:static` 会检查 `utils/*.sh` 语法，并阻止 Jenkinsfile 或报告脚本重新引入直接 `rm -rf` 清理。

`verify:local` 的 `RUN_NPM_AUDIT`、`RUN_STATIC_CHECK`、`RUN_SAFETY_CHECK` 开关只接受 `0` 或 `1`。

本地一键验证也会清理对应报告目录，并重新生成 `report/jenkins/index.html`。

`main.py` 仅保留为历史入口提示，不再包含接口调用或业务测试逻辑。

## 维护约定

- 新增接口测试时，优先在 Postman 中维护 collection，再导出到 `PostmanScene/`。
- 新增性能测试时，把 `.jmx` 放到 `script/simulate/` 或后续约定的生产脚本目录。
- JMeter 脚本里的线程数、RampUp、持续时间、思考时间和请求目标建议使用属性变量，方便 Jenkins 通过 `ThreadsCount`、`RampUp`、`time`、`ThinkTimeMs`、`TargetDomain`、`TargetPath` 覆盖。
- 接口测试失败优先看 `Allure Report`、Newman HTML 和 Jenkins JUnit 趋势。
- 性能测试分析优先看 `JMeter Dashboard`，不要用 Allure 判断 TPS/响应时间趋势。
