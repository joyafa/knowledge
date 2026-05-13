---
title: MutexLockGuard

---

# MutexLockGuard






`#include <Mutex.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[MutexLockGuard](/class_mutex_lock_guard.md#function-mutexlockguard)**(MutexLock & mutex) |
| | **[~MutexLockGuard](/class_mutex_lock_guard.md#function-~mutexlockguard)**() |

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

### function MutexLockGuard

```cpp
inline explicit MutexLockGuard(
    MutexLock & mutex
)
```


### function ~MutexLockGuard

```cpp
inline ~MutexLockGuard()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800