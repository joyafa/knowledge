---
title: muduo::net::RpcChannel

---

# muduo::net::RpcChannel






`#include <RpcChannel.h>`

Inherits from google::protobuf::RpcChannel

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[RpcChannel](/classmuduo_1_1net_1_1_rpc_channel.md#function-rpcchannel)**() |
| | **[RpcChannel](/classmuduo_1_1net_1_1_rpc_channel.md#function-rpcchannel)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| | **[~RpcChannel](/classmuduo_1_1net_1_1_rpc_channel.md#function-~rpcchannel)**() override |
| void | **[setConnection](/classmuduo_1_1net_1_1_rpc_channel.md#function-setconnection)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[setServices](/classmuduo_1_1net_1_1_rpc_channel.md#function-setservices)**(const std::map< std::string, ::google::protobuf::Service * > * services) |
| void | **[CallMethod](/classmuduo_1_1net_1_1_rpc_channel.md#function-callmethod)**(const ::google::protobuf::MethodDescriptor * method, ::google::protobuf::RpcController * controller, const ::google::protobuf::Message * request, ::google::protobuf::Message * response, ::google::protobuf::Closure * done) override |
| void | **[onMessage](/classmuduo_1_1net_1_1_rpc_channel.md#function-onmessage)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) receiveTime) |

## Public Functions Documentation

### function RpcChannel

```cpp
RpcChannel()
```


### function RpcChannel

```cpp
explicit RpcChannel(
    const TcpConnectionPtr & conn
)
```


### function ~RpcChannel

```cpp
~RpcChannel() override
```


### function setConnection

```cpp
inline void setConnection(
    const TcpConnectionPtr & conn
)
```


### function setServices

```cpp
inline void setServices(
    const std::map< std::string, ::google::protobuf::Service * > * services
)
```


### function CallMethod

```cpp
void CallMethod(
    const ::google::protobuf::MethodDescriptor * method,
    ::google::protobuf::RpcController * controller,
    const ::google::protobuf::Message * request,
    ::google::protobuf::Message * response,
    ::google::protobuf::Closure * done
) override
```


### function onMessage

```cpp
void onMessage(
    const TcpConnectionPtr & conn,
    Buffer * buf,
    Timestamp receiveTime
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800