---
title: muduo::net::TcpConnection

---

# muduo::net::TcpConnection



 [More...](#detailed-description)


`#include <TcpConnection.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md), std::enable_shared_from_this< TcpConnection >

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[TcpConnection](/classmuduo_1_1net_1_1_tcp_connection.md#function-tcpconnection)**([EventLoop](/class_event_loop.md) * loop, const string & name, int sockfd, const [InetAddress](/class_inet_address.md) & localAddr, const [InetAddress](/class_inet_address.md) & peerAddr) |
| | **[~TcpConnection](/classmuduo_1_1net_1_1_tcp_connection.md#function-~tcpconnection)**() |
| [EventLoop](/class_event_loop.md) * | **[getLoop](/classmuduo_1_1net_1_1_tcp_connection.md#function-getloop)**() const |
| const string & | **[name](/classmuduo_1_1net_1_1_tcp_connection.md#function-name)**() const |
| const [InetAddress](/class_inet_address.md) & | **[localAddress](/classmuduo_1_1net_1_1_tcp_connection.md#function-localaddress)**() const |
| const [InetAddress](/class_inet_address.md) & | **[peerAddress](/classmuduo_1_1net_1_1_tcp_connection.md#function-peeraddress)**() const |
| bool | **[connected](/classmuduo_1_1net_1_1_tcp_connection.md#function-connected)**() const |
| bool | **[disconnected](/classmuduo_1_1net_1_1_tcp_connection.md#function-disconnected)**() const |
| bool | **[getTcpInfo](/classmuduo_1_1net_1_1_tcp_connection.md#function-gettcpinfo)**(struct tcp_info * tcpi) const |
| string | **[getTcpInfoString](/classmuduo_1_1net_1_1_tcp_connection.md#function-gettcpinfostring)**() const |
| void | **[send](/classmuduo_1_1net_1_1_tcp_connection.md#function-send)**(const void * message, int len) |
| void | **[send](/classmuduo_1_1net_1_1_tcp_connection.md#function-send)**(const [StringPiece](/classmuduo_1_1_string_piece.md) & message) |
| void | **[send](/classmuduo_1_1net_1_1_tcp_connection.md#function-send)**([Buffer](/class_buffer.md) * message) |
| void | **[shutdown](/classmuduo_1_1net_1_1_tcp_connection.md#function-shutdown)**() |
| void | **[forceClose](/classmuduo_1_1net_1_1_tcp_connection.md#function-forceclose)**() |
| void | **[forceCloseWithDelay](/classmuduo_1_1net_1_1_tcp_connection.md#function-forceclosewithdelay)**(double seconds) |
| void | **[setTcpNoDelay](/classmuduo_1_1net_1_1_tcp_connection.md#function-settcpnodelay)**(bool on) |
| void | **[startRead](/classmuduo_1_1net_1_1_tcp_connection.md#function-startread)**() |
| void | **[stopRead](/classmuduo_1_1net_1_1_tcp_connection.md#function-stopread)**() |
| bool | **[isReading](/classmuduo_1_1net_1_1_tcp_connection.md#function-isreading)**() const |
| void | **[setContext](/classmuduo_1_1net_1_1_tcp_connection.md#function-setcontext)**(const boost::any & context) |
| const boost::any & | **[getContext](/classmuduo_1_1net_1_1_tcp_connection.md#function-getcontext)**() const |
| boost::any * | **[getMutableContext](/classmuduo_1_1net_1_1_tcp_connection.md#function-getmutablecontext)**() |
| void | **[setConnectionCallback](/classmuduo_1_1net_1_1_tcp_connection.md#function-setconnectioncallback)**(const [ConnectionCallback](/namespacemuduo_1_1net.md#typedef-connectioncallback) & cb) |
| void | **[setMessageCallback](/classmuduo_1_1net_1_1_tcp_connection.md#function-setmessagecallback)**(const [MessageCallback](/namespacemuduo_1_1net.md#typedef-messagecallback) & cb) |
| void | **[setWriteCompleteCallback](/classmuduo_1_1net_1_1_tcp_connection.md#function-setwritecompletecallback)**(const [WriteCompleteCallback](/namespacemuduo_1_1net.md#typedef-writecompletecallback) & cb) |
| void | **[setHighWaterMarkCallback](/classmuduo_1_1net_1_1_tcp_connection.md#function-sethighwatermarkcallback)**(const [HighWaterMarkCallback](/namespacemuduo_1_1net.md#typedef-highwatermarkcallback) & cb, size_t highWaterMark) |
| [Buffer](/class_buffer.md) * | **[inputBuffer](/classmuduo_1_1net_1_1_tcp_connection.md#function-inputbuffer)**()<br>Advanced interface.  |
| [Buffer](/class_buffer.md) * | **[outputBuffer](/classmuduo_1_1net_1_1_tcp_connection.md#function-outputbuffer)**() |
| void | **[setCloseCallback](/classmuduo_1_1net_1_1_tcp_connection.md#function-setclosecallback)**(const [CloseCallback](/namespacemuduo_1_1net.md#typedef-closecallback) & cb)<br>Internal use only.  |
| void | **[connectEstablished](/classmuduo_1_1net_1_1_tcp_connection.md#function-connectestablished)**() |
| void | **[connectDestroyed](/classmuduo_1_1net_1_1_tcp_connection.md#function-connectdestroyed)**() |

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


## Detailed Description

```cpp
class muduo::net::TcpConnection;
```


TCP connection, for both client and server usage.

This is an interface class, so don't expose too much details. 

## Public Functions Documentation

### function TcpConnection

```cpp
TcpConnection(
    EventLoop * loop,
    const string & name,
    int sockfd,
    const InetAddress & localAddr,
    const InetAddress & peerAddr
)
```


Constructs a [TcpConnection](/classmuduo_1_1net_1_1_tcp_connection.md) with a connected sockfd

User should not create this object. 


### function ~TcpConnection

```cpp
~TcpConnection()
```


### function getLoop

```cpp
inline EventLoop * getLoop() const
```


### function name

```cpp
inline const string & name() const
```


### function localAddress

```cpp
inline const InetAddress & localAddress() const
```


### function peerAddress

```cpp
inline const InetAddress & peerAddress() const
```


### function connected

```cpp
inline bool connected() const
```


### function disconnected

```cpp
inline bool disconnected() const
```


### function getTcpInfo

```cpp
bool getTcpInfo(
    struct tcp_info * tcpi
) const
```


### function getTcpInfoString

```cpp
string getTcpInfoString() const
```


### function send

```cpp
void send(
    const void * message,
    int len
)
```


### function send

```cpp
void send(
    const StringPiece & message
)
```


### function send

```cpp
void send(
    Buffer * message
)
```


### function shutdown

```cpp
void shutdown()
```


### function forceClose

```cpp
void forceClose()
```


### function forceCloseWithDelay

```cpp
void forceCloseWithDelay(
    double seconds
)
```


### function setTcpNoDelay

```cpp
void setTcpNoDelay(
    bool on
)
```


### function startRead

```cpp
void startRead()
```


### function stopRead

```cpp
void stopRead()
```


### function isReading

```cpp
inline bool isReading() const
```


### function setContext

```cpp
inline void setContext(
    const boost::any & context
)
```


### function getContext

```cpp
inline const boost::any & getContext() const
```


### function getMutableContext

```cpp
inline boost::any * getMutableContext()
```


### function setConnectionCallback

```cpp
inline void setConnectionCallback(
    const ConnectionCallback & cb
)
```


### function setMessageCallback

```cpp
inline void setMessageCallback(
    const MessageCallback & cb
)
```


### function setWriteCompleteCallback

```cpp
inline void setWriteCompleteCallback(
    const WriteCompleteCallback & cb
)
```


### function setHighWaterMarkCallback

```cpp
inline void setHighWaterMarkCallback(
    const HighWaterMarkCallback & cb,
    size_t highWaterMark
)
```


### function inputBuffer

```cpp
inline Buffer * inputBuffer()
```

Advanced interface. 

### function outputBuffer

```cpp
inline Buffer * outputBuffer()
```


### function setCloseCallback

```cpp
inline void setCloseCallback(
    const CloseCallback & cb
)
```

Internal use only. 

### function connectEstablished

```cpp
void connectEstablished()
```


### function connectDestroyed

```cpp
void connectDestroyed()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800