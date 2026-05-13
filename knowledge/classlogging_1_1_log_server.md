---
title: logging::LogServer

---

# logging::LogServer





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[LogServer](/classlogging_1_1_log_server.md#function-logserver)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr, int numThreads) |
| void | **[start](/classlogging_1_1_log_server.md#function-start)**() |

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

### function LogServer

```cpp
inline LogServer(
    EventLoop * loop,
    const InetAddress & listenAddr,
    int numThreads
)
```


### function start

```cpp
inline void start()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800