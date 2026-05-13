---
title: receiving

---

# receiving



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[onConnection](/namespacereceiving.md#function-onconnection)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[onMessage](/namespacereceiving.md#function-onmessage)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) time) |


## Functions Documentation

### function onConnection

```cpp
void onConnection(
    const TcpConnectionPtr & conn
)
```


### function onMessage

```cpp
void onMessage(
    const TcpConnectionPtr & conn,
    Buffer * buf,
    Timestamp time
)
```






-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800