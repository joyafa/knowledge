---
title: Session

---

# Session






`#include <Session.h>`

Inherits from std::enable_shared_from_this< Session >, [muduo::noncopyable](/classmuduo_1_1noncopyable.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Reader](/struct_session_1_1_reader.md)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Session](/class_session.md#function-session)**([MemcacheServer](/class_memcache_server.md) * owner, const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| | **[~Session](/class_session.md#function-~session)**() |
| | **[Session](/class_session.md#function-session)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr, const string & name, [Client](/class_client.md) * owner) |
| void | **[start](/class_session.md#function-start)**() |
| void | **[stop](/class_session.md#function-stop)**() |
| int64_t | **[bytesRead](/class_session.md#function-bytesread)**() const |
| int64_t | **[messagesRead](/class_session.md#function-messagesread)**() const |

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

### function Session

```cpp
inline Session(
    MemcacheServer * owner,
    const muduo::net::TcpConnectionPtr & conn
)
```


### function ~Session

```cpp
inline ~Session()
```


### function Session

```cpp
inline Session(
    EventLoop * loop,
    const InetAddress & serverAddr,
    const string & name,
    Client * owner
)
```


### function start

```cpp
inline void start()
```


### function stop

```cpp
inline void stop()
```


### function bytesRead

```cpp
inline int64_t bytesRead() const
```


### function messagesRead

```cpp
inline int64_t messagesRead() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800