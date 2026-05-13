---
title: muduo::net::detail

---

# muduo::net::detail



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[defaultHttpCallback](/namespacemuduo_1_1net_1_1detail.md#function-defaulthttpcallback)**(const [HttpRequest](/class_http_request.md) & , [HttpResponse](/classmuduo_1_1net_1_1_http_response.md) * resp) |
| void | **[removeConnection](/namespacemuduo_1_1net_1_1detail.md#function-removeconnection)**([EventLoop](/class_event_loop.md) * loop, const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[removeConnector](/namespacemuduo_1_1net_1_1detail.md#function-removeconnector)**(const [ConnectorPtr](/namespacemuduo_1_1net.md#typedef-connectorptr) & connector) |
| int | **[createTimerfd](/namespacemuduo_1_1net_1_1detail.md#function-createtimerfd)**() |
| void | **[readTimerfd](/namespacemuduo_1_1net_1_1detail.md#function-readtimerfd)**(int timerfd, [Timestamp](/class_timestamp.md) now) |
| struct timespec | **[howMuchTimeFromNow](/namespacemuduo_1_1net_1_1detail.md#function-howmuchtimefromnow)**([Timestamp](/class_timestamp.md) when) |
| void | **[resetTimerfd](/namespacemuduo_1_1net_1_1detail.md#function-resettimerfd)**(int timerfd, [Timestamp](/class_timestamp.md) expiration) |


## Functions Documentation

### function defaultHttpCallback

```cpp
void defaultHttpCallback(
    const HttpRequest & ,
    HttpResponse * resp
)
```


### function removeConnection

```cpp
void removeConnection(
    EventLoop * loop,
    const TcpConnectionPtr & conn
)
```


### function removeConnector

```cpp
void removeConnector(
    const ConnectorPtr & connector
)
```


### function createTimerfd

```cpp
int createTimerfd()
```


### function readTimerfd

```cpp
void readTimerfd(
    int timerfd,
    Timestamp now
)
```


### function howMuchTimeFromNow

```cpp
struct timespec howMuchTimeFromNow(
    Timestamp when
)
```


### function resetTimerfd

```cpp
void resetTimerfd(
    int timerfd,
    Timestamp expiration
)
```






-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800