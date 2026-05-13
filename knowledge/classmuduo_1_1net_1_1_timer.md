---
title: muduo::net::Timer

---

# muduo::net::Timer



 [More...](#detailed-description)


`#include <Timer.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Timer](/classmuduo_1_1net_1_1_timer.md#function-timer)**([TimerCallback](/namespacemuduo_1_1net.md#typedef-timercallback) cb, [Timestamp](/class_timestamp.md) when, double interval) |
| void | **[run](/classmuduo_1_1net_1_1_timer.md#function-run)**() const |
| [Timestamp](/class_timestamp.md) | **[expiration](/classmuduo_1_1net_1_1_timer.md#function-expiration)**() const |
| bool | **[repeat](/classmuduo_1_1net_1_1_timer.md#function-repeat)**() const |
| int64_t | **[sequence](/classmuduo_1_1net_1_1_timer.md#function-sequence)**() const |
| void | **[restart](/classmuduo_1_1net_1_1_timer.md#function-restart)**([Timestamp](/class_timestamp.md) now) |
| int64_t | **[numCreated](/classmuduo_1_1net_1_1_timer.md#function-numcreated)**() |

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
class muduo::net::Timer;
```


Internal class for timer event. 

## Public Functions Documentation

### function Timer

```cpp
inline Timer(
    TimerCallback cb,
    Timestamp when,
    double interval
)
```


### function run

```cpp
inline void run() const
```


### function expiration

```cpp
inline Timestamp expiration() const
```


### function repeat

```cpp
inline bool repeat() const
```


### function sequence

```cpp
inline int64_t sequence() const
```


### function restart

```cpp
void restart(
    Timestamp now
)
```


### function numCreated

```cpp
static inline int64_t numCreated()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800