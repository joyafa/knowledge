---
title: muduo::net::TimerQueue

---

# muduo::net::TimerQueue



 [More...](#detailed-description)


`#include <TimerQueue.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[TimerQueue](/classmuduo_1_1net_1_1_timer_queue.md#function-timerqueue)**([EventLoop](/class_event_loop.md) * loop) |
| | **[~TimerQueue](/classmuduo_1_1net_1_1_timer_queue.md#function-~timerqueue)**() |
| [TimerId](/classmuduo_1_1net_1_1_timer_id.md) | **[addTimer](/classmuduo_1_1net_1_1_timer_queue.md#function-addtimer)**([TimerCallback](/namespacemuduo_1_1net.md#typedef-timercallback) cb, [Timestamp](/class_timestamp.md) when, double interval) |
| void | **[cancel](/classmuduo_1_1net_1_1_timer_queue.md#function-cancel)**([TimerId](/classmuduo_1_1net_1_1_timer_id.md) timerId) |

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
class muduo::net::TimerQueue;
```


A best efforts timer queue. No guarantee that the callback will be on time. 

## Public Functions Documentation

### function TimerQueue

```cpp
explicit TimerQueue(
    EventLoop * loop
)
```


### function ~TimerQueue

```cpp
~TimerQueue()
```


### function addTimer

```cpp
TimerId addTimer(
    TimerCallback cb,
    Timestamp when,
    double interval
)
```


Schedules the callback to be run at given time, repeats if `interval` > 0.0.

Must be thread safe. Usually be called from other threads. 


### function cancel

```cpp
void cancel(
    TimerId timerId
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800