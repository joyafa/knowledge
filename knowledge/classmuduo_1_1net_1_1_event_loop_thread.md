---
title: muduo::net::EventLoopThread

---

# muduo::net::EventLoopThread






`#include <EventLoopThread.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void([EventLoop](/class_event_loop.md) *)> | **[ThreadInitCallback](/classmuduo_1_1net_1_1_event_loop_thread.md#typedef-threadinitcallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[EventLoopThread](/classmuduo_1_1net_1_1_event_loop_thread.md#function-eventloopthread)**(const [ThreadInitCallback](/classmuduo_1_1net_1_1_event_loop_thread.md#typedef-threadinitcallback) & cb =[ThreadInitCallback](/classmuduo_1_1net_1_1_event_loop_thread.md#typedef-threadinitcallback)(), const string & name =string()) |
| | **[~EventLoopThread](/classmuduo_1_1net_1_1_event_loop_thread.md#function-~eventloopthread)**() |
| [EventLoop](/class_event_loop.md) * | **[startLoop](/classmuduo_1_1net_1_1_event_loop_thread.md#function-startloop)**() |

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
typedef std::function<void(EventLoop*)> muduo::net::EventLoopThread::ThreadInitCallback;
```


## Public Functions Documentation

### function EventLoopThread

```cpp
EventLoopThread(
    const ThreadInitCallback & cb =ThreadInitCallback(),
    const string & name =string()
)
```


### function ~EventLoopThread

```cpp
~EventLoopThread()
```


### function startLoop

```cpp
EventLoop * startLoop()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800