---
title: muduo::net::EventLoopThreadPool

---

# muduo::net::EventLoopThreadPool






`#include <EventLoopThreadPool.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void([EventLoop](/class_event_loop.md) *)> | **[ThreadInitCallback](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#typedef-threadinitcallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[EventLoopThreadPool](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#function-eventloopthreadpool)**([EventLoop](/class_event_loop.md) * baseLoop, const string & nameArg) |
| | **[~EventLoopThreadPool](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#function-~eventloopthreadpool)**() |
| void | **[setThreadNum](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#function-setthreadnum)**(int numThreads) |
| void | **[start](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#function-start)**(const [ThreadInitCallback](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#typedef-threadinitcallback) & cb =[ThreadInitCallback](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#typedef-threadinitcallback)()) |
| [EventLoop](/class_event_loop.md) * | **[getNextLoop](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#function-getnextloop)**()<br>round-robin  |
| [EventLoop](/class_event_loop.md) * | **[getLoopForHash](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#function-getloopforhash)**(size_t hashCode)<br>with the same hash code, it will always return the same [EventLoop](/classmuduo_1_1net_1_1_event_loop.md) |
| std::vector< [EventLoop](/class_event_loop.md) * > | **[getAllLoops](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#function-getallloops)**() |
| bool | **[started](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#function-started)**() const |
| const string & | **[name](/classmuduo_1_1net_1_1_event_loop_thread_pool.md#function-name)**() const |

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

### typedef ThreadInitCallback

```cpp
typedef std::function<void(EventLoop*)> muduo::net::EventLoopThreadPool::ThreadInitCallback;
```


## Public Functions Documentation

### function EventLoopThreadPool

```cpp
EventLoopThreadPool(
    EventLoop * baseLoop,
    const string & nameArg
)
```


### function ~EventLoopThreadPool

```cpp
~EventLoopThreadPool()
```


### function setThreadNum

```cpp
inline void setThreadNum(
    int numThreads
)
```


### function start

```cpp
void start(
    const ThreadInitCallback & cb =ThreadInitCallback()
)
```


### function getNextLoop

```cpp
EventLoop * getNextLoop()
```

round-robin 

### function getLoopForHash

```cpp
EventLoop * getLoopForHash(
    size_t hashCode
)
```

with the same hash code, it will always return the same [EventLoop](/classmuduo_1_1net_1_1_event_loop.md)

### function getAllLoops

```cpp
std::vector< EventLoop * > getAllLoops()
```


### function started

```cpp
inline bool started() const
```


### function name

```cpp
inline const string & name() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800