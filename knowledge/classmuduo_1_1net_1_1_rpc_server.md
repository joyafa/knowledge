---
title: muduo::net::RpcServer

---

# muduo::net::RpcServer






`#include <RpcServer.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[RpcServer](/classmuduo_1_1net_1_1_rpc_server.md#function-rpcserver)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr) |
| void | **[setThreadNum](/classmuduo_1_1net_1_1_rpc_server.md#function-setthreadnum)**(int numThreads) |
| void | **[registerService](/classmuduo_1_1net_1_1_rpc_server.md#function-registerservice)**(::google::protobuf::Service * service) |
| void | **[start](/classmuduo_1_1net_1_1_rpc_server.md#function-start)**() |

## Public Functions Documentation

### function RpcServer

```cpp
RpcServer(
    EventLoop * loop,
    const InetAddress & listenAddr
)
```


### function setThreadNum

```cpp
inline void setThreadNum(
    int numThreads
)
```


### function registerService

```cpp
void registerService(
    ::google::protobuf::Service * service
)
```


### function start

```cpp
void start()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800