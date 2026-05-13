---
title: muduo::net::TimerId

---

# muduo::net::TimerId



 [More...](#detailed-description)


`#include <TimerId.h>`

Inherits from [muduo::copyable](/classmuduo_1_1copyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[TimerId](/classmuduo_1_1net_1_1_timer_id.md#function-timerid)**() |
| | **[TimerId](/classmuduo_1_1net_1_1_timer_id.md#function-timerid)**([Timer](/classmuduo_1_1net_1_1_timer.md) * timer, int64_t seq) |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[TimerQueue](/classmuduo_1_1net_1_1_timer_id.md#friend-timerqueue)**  |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Detailed Description

```cpp
class muduo::net::TimerId;
```


An opaque identifier, for canceling [Timer](/classmuduo_1_1net_1_1_timer.md). 

## Public Functions Documentation

### function TimerId

```cpp
inline TimerId()
```


### function TimerId

```cpp
inline TimerId(
    Timer * timer,
    int64_t seq
)
```


## Friends

### friend TimerQueue

```cpp
friend class TimerQueue(
    TimerQueue 
);
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800