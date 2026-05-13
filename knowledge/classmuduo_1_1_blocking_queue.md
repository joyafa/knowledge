---
title: muduo::BlockingQueue

---

# muduo::BlockingQueue



 [More...](#detailed-description)


`#include <BlockingQueue.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| using std::deque< [T](/classmuduo_1_1_t.md) > | **[queue_type](/classmuduo_1_1_blocking_queue.md#using-queue-type)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BlockingQueue](/classmuduo_1_1_blocking_queue.md#function-blockingqueue)**() |
| void | **[put](/classmuduo_1_1_blocking_queue.md#function-put)**(const [T](/classmuduo_1_1_t.md) & x) |
| void | **[put](/classmuduo_1_1_blocking_queue.md#function-put)**([T](/classmuduo_1_1_t.md) && x) |
| [T](/classmuduo_1_1_t.md) | **[take](/classmuduo_1_1_blocking_queue.md#function-take)**() |
| [queue_type](/classmuduo_1_1_blocking_queue.md#using-queue-type) | **[drain](/classmuduo_1_1_blocking_queue.md#function-drain)**() |
| size_t | **[size](/classmuduo_1_1_blocking_queue.md#function-size)**() const |

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
class muduo::BlockingQueue;
```

## Public Types Documentation

### using queue_type

```cpp
using muduo::BlockingQueue< T >::queue_type = std::deque<T>;
```


## Public Functions Documentation

### function BlockingQueue

```cpp
inline BlockingQueue()
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


### function drain

```cpp
inline queue_type drain()
```


### function size

```cpp
inline size_t size() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800