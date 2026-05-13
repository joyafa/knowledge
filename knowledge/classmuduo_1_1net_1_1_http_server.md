---
title: muduo::net::HttpServer

---

# muduo::net::HttpServer



 [More...](#detailed-description)


`#include <HttpServer.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(const [HttpRequest](/class_http_request.md) &, [HttpResponse](/classmuduo_1_1net_1_1_http_response.md) *)> | **[HttpCallback](/classmuduo_1_1net_1_1_http_server.md#typedef-httpcallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HttpServer](/classmuduo_1_1net_1_1_http_server.md#function-httpserver)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr, const string & name, [TcpServer::Option](/classmuduo_1_1net_1_1_tcp_server.md#enum-option) option =[TcpServer::kNoReusePort](/classmuduo_1_1net_1_1_tcp_server.md#enumvalue-knoreuseport)) |
| [EventLoop](/class_event_loop.md) * | **[getLoop](/classmuduo_1_1net_1_1_http_server.md#function-getloop)**() const |
| void | **[setHttpCallback](/classmuduo_1_1net_1_1_http_server.md#function-sethttpcallback)**(const [HttpCallback](/classmuduo_1_1net_1_1_http_server.md#typedef-httpcallback) & cb)<br>Not thread safe, callback be registered before calling [start()]().  |
| void | **[setThreadNum](/classmuduo_1_1net_1_1_http_server.md#function-setthreadnum)**(int numThreads) |
| void | **[start](/classmuduo_1_1net_1_1_http_server.md#function-start)**() |

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
class muduo::net::HttpServer;
```


A simple embeddable HTTP server designed for report status of a program. It is not a fully HTTP 1.1 compliant server, but provides minimum features that can communicate with HttpClient and Web browser. It is synchronous, just like Java Servlet. 

## Public Types Documentation

### typedef HttpCallback

```cpp
typedef std::function<void (const HttpRequest&, HttpResponse*)> muduo::net::HttpServer::HttpCallback;
```


## Public Functions Documentation

### function HttpServer

```cpp
HttpServer(
    EventLoop * loop,
    const InetAddress & listenAddr,
    const string & name,
    TcpServer::Option option =TcpServer::kNoReusePort
)
```


### function getLoop

```cpp
inline EventLoop * getLoop() const
```


### function setHttpCallback

```cpp
inline void setHttpCallback(
    const HttpCallback & cb
)
```

Not thread safe, callback be registered before calling [start()](). 

### function setThreadNum

```cpp
inline void setThreadNum(
    int numThreads
)
```


### function start

```cpp
void start()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800