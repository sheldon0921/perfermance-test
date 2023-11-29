#  												接口自动化解决方案V1.0

## 一、目的

​		随着业务扩张，普通的手工测试已经无法满足现阶段的需求。市场上接口自动化测试框架层出不群，但是普遍对测试人员的技能要求较高。为了提高测试覆盖率，进而提升测试质量，提高系统可用性。因此我们将python+requests+pytest和postman+Newman两套方案整理到一个工程里面；对于有一定编码能力的自动化测试组人员（Auto Tester）使用python+requests+pytest对比较复杂的场景进行覆盖；针对于没有编码基础或者编码基础比较薄弱的功能测试人员（TE）则使用postman+Newman对简单场景进行接口层面的覆盖。️

## 二、目录结构

```
postmanapi
├────	PostmanScene					 postman导出的json脚本			
│	└─── CommunityGroupBuying	                 社区团购版
│	│		└─── CommunityGroupBuying.json   社区团购版json脚本
│	└─── DirectStoreVersion			         直营连锁版
│       │ 		└── DirectStore.json             直营连锁版json脚本
│	└─── HaveStoreVersion			         中心商城有门店版
│       │		└── HaveStore.json	         中心商城有门店版json脚本
│	└─── NoStoreVersion			         中心商城无门的版
│    			└── Nostore.json		 中心商城无门的版json脚本
├──── config
│	└───environment.ini                              环境配置信息
├──── data					         测试数据
├──── img				                 README图片数据
├──── log						 格式化日志输出及日志级别
├──── report						 测试报告
├──── tests					         Auto Tester提交的pytest用例
├──── utils						 工具
│	└───myJson.py		                         json数据处理
│	└───myTime.py				         自定义时间戳/格式化输出时间
│	└───readerFile.py			         文件读取
│	└───readerIniFile.py			         读取配置文件
├──── JenkinsFile				         工程构建脚本
├──── mian.py					         pytest用例执行入口文件
├──── CollectionApi.sh			                 postman json用例收集
├──── package.json
├──── package-lock.json
├──── Pipfile					         python环境配置
├──── pytest.ini					 pytest配置
├──── requirements.txt				         pytest依赖库
├──── README						 介绍文档
```
## 三、python3+pytest使用
### 3.1开发环境搭建

#### 3.1.1依赖
* python 3.5+
* pipenv
1. python 安装
2. pipenv 安装
```bash
pip install pipenv
```
3. 初始化工作环境
```bash
pipenv install
```
### 3.2测试用例编写规范

1. 测试用例必须放在 `tests` 目录或其子目录下
2. 测试文件名称必须以 `_test.py` 结尾
3. 测试用例必须以 `Test` 结尾
4. 测试方法必须以 `test_` 开始

**Example**: demo_test.py

```python
from tests.helper import ShopTest

class DemoTest(ShopTest):

    def test_demo1(self):
        self.assertTrue(1=1, 'test_demo1')
        
    def test_demo2(self):
        self.assertTrue(1=1, 'test_demo2')
```

### 3.3开发执行
```bash
pipenv run pytest 
# or 生产报告
pipenv run pytest --junit-xml=report/results.xml --html=report/results.html --self-contained-html
```

或执行 `main.py`

### 3.4 DDT 使用规范

1. 不允许一个测试用例里面存在针对多个接口的测试（不易于问题排查和多人合作）
2. 数据中不允许包含业务逻辑，可以包含：输入参数、断言参数、配置参数
3. 支持 ddt 测试方法的参数必须是命名参数
4. ddt 测试需要使用 @unpack 注解
5. 传入 ddt 测试的数据必须是数组
6. 每个 testcase 一个数据文件

**Example**: `yaml`

`tests/data/demo.yaml`：
```yaml
data_set1:
  -
    a: 1
    b: 2
    expected: 3
  -
    a: 3
    b: 3
    expected: 6

data_set2:
  -
    sub1: 6
    sub2: 4
    expected: 2
  -
    sub1: 4
    sub2: 1
    expected: 3
```
```python
from ddt import ddt, unpack, data

from atr.reader import read_yaml
from atr.testcase import BaseTest

yaml_demo_data = read_yaml('tests/data/demo.yaml')


@ddt
class YamlReaderTest(BaseTest):

    @data(*yaml_demo_data['data_set1'])
    @unpack
    def test_add(self, a, b, expected):
        act = a + b
        self.assertEqual(act, expected)

    @data(*yaml_demo_data['data_set2'])
    @unpack
    def test_sub(self, sub1, sub2, expected):
        act = sub1 - sub2
        self.assertEqual(act, expected)

```
**Example**: `json`
`tests/data/demo.json` ：
```json
{
  "data_set1": [
    {
      "a": 1,
      "b": 2,
      "expected": 3
    },
    {
      "a": 3,
      "b": 3,
      "expected": 6
    }
  ],
  "data_set2": [
    {
      "sub1": 6,
      "sub2": 4,
      "expected": 2
    },
    {
      "sub1": 4,
      "sub2": 1,
      "expected": 3
    }
  ]
}
```
```python
from ddt import ddt, unpack, data

from atr.reader import read_json
from atr.testcase import BaseTest

json_demo_data = read_json('tests/data/demo.json')

@ddt
class JsonReaderTest(BaseTest):
    @data(*json_demo_data['data_set1'])
    @unpack
    def test_add(self, a, b, expected):
        act = a + b
        self.assertEqual(act, expected)

    @data(*json_demo_data['data_set2'])
    @unpack
    def test_sub(self, sub1, sub2, expected):
        act = sub1 - sub2
        self.assertEqual(act, expected)

```
## 四、Postman + newman
### 4.1 开发环境搭建
    1、安装nodejs（Node.js >= v10）;
    2、克隆项目至本地：git clone ssh://git@gitlab-ce.k8s.tools.vchangyi.com:32201/tester/api-automated-testing.git
    3、cd 至项目根目录执行 npm install 安装依赖
    4、安装postman
### 4.2、用到的技术

​	1、Postman使用

​	2、Newman（TE可以不用了解）

​	3、Jenkins（TE可以不用了解）

​	4、js基本语法（TE可以不用了解，稍作学习可做断言即可）

### 4.3、实施流程

![image-20210310190524864](data/img/image-20210310190524864.png)

### 4.4、具体实施步骤

#### 4.4.1、postman接口录入

![image-20210310190846526](data/img/image-20210310190846526.png)

#### 4.4.2、变量参数化定义

![image-20210310190954783](data/img/image-20210310190954783.png)

![image-20210310191026632](data/img/image-20210310191026632.png)

![image-20210310191329688](data/img/image-20210310191329688.png)

#### 4.4.3、变量使用

![image-20210310191139041](data/img/image-20210310191139041.png)

![image-20210310191218586](data/img/image-20210310191218586.png)

![image-20210310191420779](data/img/image-20210310191420779.png)

#### 4.4.4、用例添加断言

​		postman有丰富的断言库，可直接点击左侧断言类型快速生成断言的js脚本，稍作修改便可生成一个断言！

![image-20210310192120924](data/img/image-20210310192120924.png)

![image-20210310191846033](data/img/image-20210310191846033.png)

### 4.4.5、脚本导出

![image-20210310192319146](data/img/image-20210310192319146.png)

![image-20210310192344557](data/img/image-20210310192344557.png)

## 4.5、Jenkins构建

![image-20210310192708424](data/img/image-20210310192708424.png)

#### ![image-20210310194033912](data/img/image-20210310194033912.png)	

### 4.5.1 构建脚本

​					<!--这个构建脚本主要实现了工作目录下json格式的用例的收集/执行功能-->

```sh
#！/usr/bin/bash
echo "配置npm环境变量："
source /etc/profile
echo "newman版本："
newman -version
echo "执行测试用例："
function buildFunction(){
for file in ` ls $1`
do
    if [[ -d $1"/"${file} ]]
    then
    buildFunction $1"/"${file}
    else
        local path=$1"/"${file}
        local name=${file}
        if [[ ${name} == *json ]]
        then
            newman run ${path}
        fi
    fi
done
}
INIT_PATH="api/"
buildFunction ${INIT_PATH}
```

#### 4.5.2 构建日志
#### ![image-20210310193047380](data/img/image-20210310193047380.png)
----------------------------------------------------------当有断言失败时整个构建就会失败--------------------------------------------------

**OVER**

