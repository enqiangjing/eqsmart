# eqsmart
基于Python，简单的微服务框架。

```
# 注册中心框架
https://github.com/enqiangjing/eqlink

# 注册中心服务示例工程
https://github.com/enqiangjing/eqlink-server
```

## 1. 使用说明
启动中注册中心——启动服务提供者——启动服务消费者——启动网关服务。  
实际使用过程中：服务消费者往往同时也是服务提供者；网关在提供HTTP服务的同时，也是服务消费者。  
eqlink-server 会自动移除失效服务，eqlink-server 下线后 consumer 会重试一定次数（根据配置）再次连接注册中心。  

**注意**
```
1、所有 provider 提供的服务不能重名。
2、provider 添加新的服务或接口，一定时间（配置）后才能被 consumer 同步到。
```

### 1.1 服务提供者 Provider
```
# 示例工程
https://github.com/enqiangjing/eqsmart-provider
```

### 1.2 服务消费者 Consumer
```
# 示例工程
https://github.com/enqiangjing/eqsmart-consumer
```

### 1.3 网关服务 Gateway
```
# 示例工程
https://github.com/enqiangjing/eqsmart-gateway
```

## 2. 使用测试
向网关发送请求，获得响应结果。
### 2.1 Test Function A
**request**
> POST http://127.0.0.1:7001/api_a/func_a
```json

{
    "a": "test a",
    "b": "test b"
}
```
**response**
```json
{
    "remote_a": {
        "remote_a": {
            "provider_a": "aa ++ ab"
        },
        "func_consumer_a": "a-a -- a-b",
        "application_name": "Consumer"
    },
    "api_a_func_a": "test a -- test b",
    "application_name": "Gateway"
}
```
### 2.2 Test Function B
**request**
> POST http://127.0.0.1:7001/api_b/func_b
```json

{
    "a": "test a",
    "b": "test b"
}
```
**response**
```json
{
    "remote_b": {
        "remote_b": {
            "provider_b": "ba ++ bb"
        },
        "func_consumer_b": "b-a -- b-b",
        "application_name": "Consumer"
    },
    "api_b_func_b": "test a -- test b",
    "application_name": "Gateway"
}
```


## * 免责声明
* 本项目所有内容仅供参考和学习交流使用。
* 项目所存在的风险将由使用者自行承担，因使用本项目而产生的一切后果也由使用者自己承担。
* 凡以任何方式直接、间接使用本项目的人员，视为自愿接受本项目声明和法律法规的约束。