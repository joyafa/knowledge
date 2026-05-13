---
title: muduo::ThreadLocal

---

# muduo::ThreadLocal



 [More...](#detailed-description)


`#include <ThreadLocal.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ThreadLocal](/classmuduo_1_1_thread_local.md#function-threadlocal)**() |
| | **[~ThreadLocal](/classmuduo_1_1_thread_local.md#function-~threadlocal)**() |
| [T](/classmuduo_1_1_t.md) & | **[value](/classmuduo_1_1_thread_local.md#function-value)**() |

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
template <typename T >
class muduo::ThreadLocal;
```

## Public Functions Documentation

### function ThreadLocal

```cpp
inline ThreadLocal()
```


### function ~ThreadLocal

```cpp
inline ~ThreadLocal()
```


### function value

```cpp
inline T & value()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800