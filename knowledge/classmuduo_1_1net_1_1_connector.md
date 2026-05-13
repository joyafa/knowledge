---
title: muduo::net::Connector

---

# muduo::net::Connector






`#include <Connector.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md), std::enable_shared_from_this< Connector >

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(int sockfd)> | **[NewConnectionCallback](/classmuduo_1_1net_1_1_connector.md#typedef-newconnectioncallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Connector](/classmuduo_1_1net_1_1_connector.md#function-connector)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr) |
| | **[~Connector](/classmuduo_1_1net_1_1_connector.md#function-~connector)**() |
| void | **[setNewConnectionCallback](/classmuduo_1_1net_1_1_connector.md#function-setnewconnectioncallback)**(const [NewConnectionCallback](/classmuduo_1_1net_1_1_connector.md#typedef-newconnectioncallback) & cb) |
| void | **[start](/classmuduo_1_1net_1_1_connector.md#function-start)**() |
| void | **[restart](/classmuduo_1_1net_1_1_connector.md#function-restart)**() |
| void | **[stop](/classmuduo_1_1net_1_1_connector.md#function-stop)**() |
| const [InetAddress](/class_inet_address.md) & | **[serverAddress](/classmuduo_1_1net_1_1_connector.md#function-serveraddress)**() const |

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


## Public Types Documentation

### typedef NewConnectionCallback

```cpp
typedef std::function<void (int sockfd)> muduo::net::Connector::NewConnectionCallback;
```


## Public Functions Documentation

### function Connector

```cpp
Connector(
    EventLoop * loop,
    const InetAddress & serverAddr
)
```


### function ~Connector

```cpp
~Connector()
```


### function setNewConnectionCallback

```cpp
inline void setNewConnectionCallback(
    const NewConnectionCallback & cb
)
```


### function start

```cpp
void start()
```


### function restart

```cpp
void restart()
```


### function stop

```cpp
void stop()
```


### function serverAddress

```cpp
inline const InetAddress & serverAddress() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800