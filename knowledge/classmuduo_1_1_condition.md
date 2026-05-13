---
title: muduo::Condition

---

# muduo::Condition






`#include <Condition.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Condition](/classmuduo_1_1_condition.md#function-condition)**(MutexLock & mutex) |
| | **[~Condition](/classmuduo_1_1_condition.md#function-~condition)**() |
| void | **[wait](/classmuduo_1_1_condition.md#function-wait)**() |
| bool | **[waitForSeconds](/classmuduo_1_1_condition.md#function-waitforseconds)**(double seconds) |
| void | **[notify](/classmuduo_1_1_condition.md#function-notify)**() |
| void | **[notifyAll](/classmuduo_1_1_condition.md#function-notifyall)**() |

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

### function Condition

```cpp
inline explicit Condition(
    MutexLock & mutex
)
```


### function ~Condition

```cpp
inline ~Condition()
```


### function wait

```cpp
inline void wait()
```


### function waitForSeconds

```cpp
bool waitForSeconds(
    double seconds
)
```


### function notify

```cpp
inline void notify()
```


### function notifyAll

```cpp
inline void notifyAll()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800