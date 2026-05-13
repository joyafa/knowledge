---
title: muduo::net::Acceptor

---

# muduo::net::Acceptor



 [More...](#detailed-description)


`#include <Acceptor.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(int sockfd, const [InetAddress](/class_inet_address.md) &)> | **[NewConnectionCallback](/classmuduo_1_1net_1_1_acceptor.md#typedef-newconnectioncallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Acceptor](/classmuduo_1_1net_1_1_acceptor.md#function-acceptor)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr, bool reuseport) |
| | **[~Acceptor](/classmuduo_1_1net_1_1_acceptor.md#function-~acceptor)**() |
| void | **[setNewConnectionCallback](/classmuduo_1_1net_1_1_acceptor.md#function-setnewconnectioncallback)**(const [NewConnectionCallback](/classmuduo_1_1net_1_1_acceptor.md#typedef-newconnectioncallback) & cb) |
| void | **[listen](/classmuduo_1_1net_1_1_acceptor.md#function-listen)**() |
| bool | **[listening](/classmuduo_1_1net_1_1_acceptor.md#function-listening)**() const |

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
class muduo::net::Acceptor;
```


[Acceptor](/classmuduo_1_1net_1_1_acceptor.md) of incoming TCP connections. 

## Public Types Documentation

### typedef NewConnectionCallback

```cpp
typedef std::function<void (int sockfd, const InetAddress&)> muduo::net::Acceptor::NewConnectionCallback;
```


## Public Functions Documentation

### function Acceptor

```cpp
Acceptor(
    EventLoop * loop,
    const InetAddress & listenAddr,
    bool reuseport
)
```


### function ~Acceptor

```cpp
~Acceptor()
```


### function setNewConnectionCallback

```cpp
inline void setNewConnectionCallback(
    const NewConnectionCallback & cb
)
```


### function listen

```cpp
void listen()
```


### function listening

```cpp
inline bool listening() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800