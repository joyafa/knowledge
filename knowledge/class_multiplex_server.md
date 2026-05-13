---
title: MultiplexServer

---

# MultiplexServer





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[MultiplexServer](/class_multiplex_server.md#function-multiplexserver)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr, const [InetAddress](/class_inet_address.md) & backendAddr, int numThreads) |
| void | **[start](/class_multiplex_server.md#function-start)**() |
| | **[MultiplexServer](/class_multiplex_server.md#function-multiplexserver)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr, const [InetAddress](/class_inet_address.md) & backendAddr) |
| void | **[start](/class_multiplex_server.md#function-start)**() |

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

### function MultiplexServer

```cpp
inline MultiplexServer(
    EventLoop * loop,
    const InetAddress & listenAddr,
    const InetAddress & backendAddr,
    int numThreads
)
```


### function start

```cpp
inline void start()
```


### function MultiplexServer

```cpp
inline MultiplexServer(
    EventLoop * loop,
    const InetAddress & listenAddr,
    const InetAddress & backendAddr
)
```


### function start

```cpp
inline void start()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800