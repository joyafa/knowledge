---
title: muduo::BoundedBlockingQueue

---

# muduo::BoundedBlockingQueue



 [More...](#detailed-description)


`#include <BoundedBlockingQueue.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BoundedBlockingQueue](/classmuduo_1_1_bounded_blocking_queue.md#function-boundedblockingqueue)**(int maxSize) |
| void | **[put](/classmuduo_1_1_bounded_blocking_queue.md#function-put)**(const [T](/classmuduo_1_1_t.md) & x) |
| void | **[put](/classmuduo_1_1_bounded_blocking_queue.md#function-put)**([T](/classmuduo_1_1_t.md) && x) |
| [T](/classmuduo_1_1_t.md) | **[take](/classmuduo_1_1_bounded_blocking_queue.md#function-take)**() |
| bool | **[empty](/classmuduo_1_1_bounded_blocking_queue.md#function-empty)**() const |
| bool | **[full](/classmuduo_1_1_bounded_blocking_queue.md#function-full)**() const |
| size_t | **[size](/classmuduo_1_1_bounded_blocking_queue.md#function-size)**() const |
| size_t | **[capacity](/classmuduo_1_1_bounded_blocking_queue.md#function-capacity)**() const |

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
class muduo::BoundedBlockingQueue;
```

## Public Functions Documentation

### function BoundedBlockingQueue

```cpp
inline explicit BoundedBlockingQueue(
    int maxSize
)
```


### function put

```cpp
inline void put(
    const T & x
)
```


### function put

```cpp
inline void put(
    T && x
)
```


### function take

```cpp
inline T take()
```


### function empty

```cpp
inline bool empty() const
```


### function full

```cpp
inline bool full() const
```


### function size

```cpp
inline size_t size() const
```


### function capacity

```cpp
inline size_t capacity() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800