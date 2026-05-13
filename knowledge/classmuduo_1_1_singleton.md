---
title: muduo::Singleton

---

# muduo::Singleton



 [More...](#detailed-description)


`#include <Singleton.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Singleton](/classmuduo_1_1_singleton.md#function-singleton)**() =delete |
| | **[~Singleton](/classmuduo_1_1_singleton.md#function-~singleton)**() =delete |
| [T](/classmuduo_1_1_t.md) & | **[instance](/classmuduo_1_1_singleton.md#function-instance)**() |

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
class muduo::Singleton;
```

## Public Functions Documentation

### function Singleton

```cpp
Singleton() =delete
```


### function ~Singleton

```cpp
~Singleton() =delete
```


### function instance

```cpp
static inline T & instance()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800