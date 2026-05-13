---
title: muduo::net::TcpServer

---

# muduo::net::TcpServer



 [More...](#detailed-description)


`#include <TcpServer.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[Option](/classmuduo_1_1net_1_1_tcp_server.md#enum-option)** { kNoReusePort, kReusePort} |
| typedef std::function< void([EventLoop](/class_event_loop.md) *)> | **[ThreadInitCallback](/classmuduo_1_1net_1_1_tcp_server.md#typedef-threadinitcallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[TcpServer](/classmuduo_1_1net_1_1_tcp_server.md#function-tcpserver)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr, const string & nameArg, [Option](/classmuduo_1_1net_1_1_tcp_server.md#enum-option) option =[kNoReusePort](/classmuduo_1_1net_1_1_tcp_server.md#enumvalue-knoreuseport)) |
| | **[~TcpServer](/classmuduo_1_1net_1_1_tcp_server.md#function-~tcpserver)**() |
| const string & | **[ipPort](/classmuduo_1_1net_1_1_tcp_server.md#function-ipport)**() const |
| const string & | **[name](/classmuduo_1_1net_1_1_tcp_server.md#function-name)**() const |
| [EventLoop](/class_event_loop.md) * | **[getLoop](/classmuduo_1_1net_1_1_tcp_server.md#function-getloop)**() const |
| void | **[setThreadNum](/classmuduo_1_1net_1_1_tcp_server.md#function-setthreadnum)**(int numThreads) |
| void | **[setThreadInitCallback](/classmuduo_1_1net_1_1_tcp_server.md#function-setthreadinitcallback)**(const [ThreadInitCallback](/classmuduo_1_1net_1_1_tcp_server.md#typedef-threadinitcallback) & cb) |
| std::shared_ptr< [EventLoopThreadPool](/classmuduo_1_1net_1_1_event_loop_thread_pool.md) > | **[threadPool](/classmuduo_1_1net_1_1_tcp_server.md#function-threadpool)**()<br>valid after calling [start()]() |
| void | **[start](/classmuduo_1_1net_1_1_tcp_server.md#function-start)**() |
| void | **[setConnectionCallback](/classmuduo_1_1net_1_1_tcp_server.md#function-setconnectioncallback)**(const [ConnectionCallback](/namespacemuduo_1_1net.md#typedef-connectioncallback) & cb) |
| void | **[setMessageCallback](/classmuduo_1_1net_1_1_tcp_server.md#function-setmessagecallback)**(const [MessageCallback](/namespacemuduo_1_1net.md#typedef-messagecallback) & cb) |
| void | **[setWriteCompleteCallback](/classmuduo_1_1net_1_1_tcp_server.md#function-setwritecompletecallback)**(const [WriteCompleteCallback](/namespacemuduo_1_1net.md#typedef-writecompletecallback) & cb) |

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
class muduo::net::TcpServer;
```


TCP server, supports single-threaded and thread-pool models.

This is an interface class, so don't expose too much details. 

## Public Types Documentation

### enum Option

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kNoReusePort | |   |
| kReusePort | |   |




### typedef ThreadInitCallback

```cpp
typedef std::function<void(EventLoop*)> muduo::net::TcpServer::ThreadInitCallback;
```


## Public Functions Documentation

### function TcpServer

```cpp
TcpServer(
    EventLoop * loop,
    const InetAddress & listenAddr,
    const string & nameArg,
    Option option =kNoReusePort
)
```


### function ~TcpServer

```cpp
~TcpServer()
```


### function ipPort

```cpp
inline const string & ipPort() const
```


### function name

```cpp
inline const string & name() const
```


### function getLoop

```cpp
inline EventLoop * getLoop() const
```


### function setThreadNum

```cpp
void setThreadNum(
    int numThreads
)
```


**Parameters**: 

  * **numThreads** 

* 0 means all I/O in loop's thread, no thread will created. this is the default value.
* 1 means all I/O in another thread.
* N means a thread pool with N threads, new connections are assigned on a round-robin basis. 


Set the number of threads for handling input.

Always accepts new connection in loop's thread. Must be called before `start`


### function setThreadInitCallback

```cpp
inline void setThreadInitCallback(
    const ThreadInitCallback & cb
)
```


### function threadPool

```cpp
inline std::shared_ptr< EventLoopThreadPool > threadPool()
```

valid after calling [start()]()

### function start

```cpp
void start()
```


Starts the server if it's not listening.

It's harmless to call it multiple times. [Thread](/classmuduo_1_1_thread.md) safe. 


### function setConnectionCallback

```cpp
inline void setConnectionCallback(
    const ConnectionCallback & cb
)
```


Set connection callback. Not thread safe. 


### function setMessageCallback

```cpp
inline void setMessageCallback(
    const MessageCallback & cb
)
```


Set message callback. Not thread safe. 


### function setWriteCompleteCallback

```cpp
inline void setWriteCompleteCallback(
    const WriteCompleteCallback & cb
)
```


Set write complete callback. Not thread safe. 


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800