---
title: muduo::ThreadLocalSingleton

---

# muduo::ThreadLocalSingleton



 [More...](#detailed-description)


`#include <ThreadLocalSingleton.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ThreadLocalSingleton](/classmuduo_1_1_thread_local_singleton.md#function-threadlocalsingleton)**() =delete |
| | **[~ThreadLocalSingleton](/classmuduo_1_1_thread_local_singleton.md#function-~threadlocalsingleton)**() =delete |
| [T](/classmuduo_1_1_t.md) & | **[instance](/classmuduo_1_1_thread_local_singleton.md#function-instance)**() |
| [T](/classmuduo_1_1_t.md) * | **[pointer](/classmuduo_1_1_thread_local_singleton.md#function-pointer)**() |

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
class muduo::ThreadLocalSingleton;
```

## Public Functions Documentation

### function ThreadLocalSingleton

```cpp
ThreadLocalSingleton() =delete
```


### function ~ThreadLocalSingleton

```cpp
~ThreadLocalSingleton() =delete
```


### function instance

```cpp
static inline T & instance()
```


### function pointer

```cpp
static inline T * pointer()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800