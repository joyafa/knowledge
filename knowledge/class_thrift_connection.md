---
title: ThriftConnection

---

# ThriftConnection






`#include <ThriftConnection.h>`

Inherits from boost::noncopyable, boost::enable_shared_from_this< ThriftConnection >

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[State](/class_thrift_connection.md#enum-state)** { kExpectFrameSize, kExpectFrame} |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ThriftConnection](/class_thrift_connection.md#function-thriftconnection)**([ThriftServer](/class_thrift_server.md) * server, const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |

## Public Types Documentation

### enum State

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kExpectFrameSize | |   |
| kExpectFrame | |   |




## Public Functions Documentation

### function ThriftConnection

```cpp
ThriftConnection(
    ThriftServer * server,
    const muduo::net::TcpConnectionPtr & conn
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800