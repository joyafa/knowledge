---
title: muduo::net::TcpClient

---

# muduo::net::TcpClient






`#include <TcpClient.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[TcpClient](/classmuduo_1_1net_1_1_tcp_client.md#function-tcpclient)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr, const string & nameArg) |
| | **[~TcpClient](/classmuduo_1_1net_1_1_tcp_client.md#function-~tcpclient)**() |
| void | **[connect](/classmuduo_1_1net_1_1_tcp_client.md#function-connect)**() |
| void | **[disconnect](/classmuduo_1_1net_1_1_tcp_client.md#function-disconnect)**() |
| void | **[stop](/classmuduo_1_1net_1_1_tcp_client.md#function-stop)**() |
| [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) | **[connection](/classmuduo_1_1net_1_1_tcp_client.md#function-connection)**() const |
| [EventLoop](/class_event_loop.md) * | **[getLoop](/classmuduo_1_1net_1_1_tcp_client.md#function-getloop)**() const |
| bool | **[retry](/classmuduo_1_1net_1_1_tcp_client.md#function-retry)**() const |
| void | **[enableRetry](/classmuduo_1_1net_1_1_tcp_client.md#function-enableretry)**() |
| const string & | **[name](/classmuduo_1_1net_1_1_tcp_client.md#function-name)**() const |
| void | **[setConnectionCallback](/classmuduo_1_1net_1_1_tcp_client.md#function-setconnectioncallback)**([ConnectionCallback](/namespacemuduo_1_1net.md#typedef-connectioncallback) cb) |
| void | **[setMessageCallback](/classmuduo_1_1net_1_1_tcp_client.md#function-setmessagecallback)**([MessageCallback](/namespacemuduo_1_1net.md#typedef-messagecallback) cb) |
| void | **[setWriteCompleteCallback](/classmuduo_1_1net_1_1_tcp_client.md#function-setwritecompletecallback)**([WriteCompleteCallback](/namespacemuduo_1_1net.md#typedef-writecompletecallback) cb) |

## Additional inherited members

**Public Functions inherited from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**(const noncopyable & ) =delete |
| void | **[operator=](/classmuduo_1_1noncopyable.md#function-operator=)**(const [noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable) & ) =delete |

**Protected Functions inherited from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**() =default |
| | **[~noncopyable](/classmuduo_1_1noncopyable.md#function-~noncopyable)**() =default |


## Public Functions Documentation

### function TcpClient

```cpp
TcpClient(
    EventLoop * loop,
    const InetAddress & serverAddr,
    const string & nameArg
)
```


### function ~TcpClient

```cpp
~TcpClient()
```


### function connect

```cpp
void connect()
```


### function disconnect

```cpp
void disconnect()
```


### function stop

```cpp
void stop()
```


### function connection

```cpp
inline TcpConnectionPtr connection() const
```


### function getLoop

```cpp
inline EventLoop * getLoop() const
```


### function retry

```cpp
inline bool retry() const
```


### function enableRetry

```cpp
inline void enableRetry()
```


### function name

```cpp
inline const string & name() const
```


### function setConnectionCallback

```cpp
inline void setConnectionCallback(
    ConnectionCallback cb
)
```


Set connection callback. Not thread safe. 


### function setMessageCallback

```cpp
inline void setMessageCallback(
    MessageCallback cb
)
```


Set message callback. Not thread safe. 


### function setWriteCompleteCallback

```cpp
inline void setWriteCompleteCallback(
    WriteCompleteCallback cb
)
```


Set write complete callback. Not thread safe. 


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800