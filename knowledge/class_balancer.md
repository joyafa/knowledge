---
title: Balancer

---

# Balancer





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Balancer](/class_balancer.md#function-balancer)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr, const string & name, const std::vector< [InetAddress](/class_inet_address.md) > & backends) |
| | **[~Balancer](/class_balancer.md#function-~balancer)**() |
| void | **[setThreadNum](/class_balancer.md#function-setthreadnum)**(int numThreads) |
| void | **[start](/class_balancer.md#function-start)**() |
| | **[Balancer](/class_balancer.md#function-balancer)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr, const string & name, const std::vector< [InetAddress](/class_inet_address.md) > & backends) |
| | **[~Balancer](/class_balancer.md#function-~balancer)**() |
| void | **[setThreadNum](/class_balancer.md#function-setthreadnum)**(int numThreads) |
| void | **[start](/class_balancer.md#function-start)**() |

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

### function Balancer

```cpp
inline Balancer(
    EventLoop * loop,
    const InetAddress & listenAddr,
    const string & name,
    const std::vector< InetAddress > & backends
)
```


### function ~Balancer

```cpp
inline ~Balancer()
```


### function setThreadNum

```cpp
inline void setThreadNum(
    int numThreads
)
```


### function start

```cpp
inline void start()
```


### function Balancer

```cpp
inline Balancer(
    EventLoop * loop,
    const InetAddress & listenAddr,
    const string & name,
    const std::vector< InetAddress > & backends
)
```


### function ~Balancer

```cpp
inline ~Balancer()
```


### function setThreadNum

```cpp
inline void setThreadNum(
    int numThreads
)
```


### function start

```cpp
inline void start()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800