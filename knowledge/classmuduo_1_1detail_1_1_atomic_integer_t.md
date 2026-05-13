---
title: muduo::detail::AtomicIntegerT

---

# muduo::detail::AtomicIntegerT



 [More...](#detailed-description)


`#include <Atomic.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[AtomicIntegerT](/classmuduo_1_1detail_1_1_atomic_integer_t.md#function-atomicintegert)**() |
| [T](/classmuduo_1_1_t.md) | **[get](/classmuduo_1_1detail_1_1_atomic_integer_t.md#function-get)**() |
| [T](/classmuduo_1_1_t.md) | **[getAndAdd](/classmuduo_1_1detail_1_1_atomic_integer_t.md#function-getandadd)**([T](/classmuduo_1_1_t.md) x) |
| [T](/classmuduo_1_1_t.md) | **[addAndGet](/classmuduo_1_1detail_1_1_atomic_integer_t.md#function-addandget)**([T](/classmuduo_1_1_t.md) x) |
| [T](/classmuduo_1_1_t.md) | **[incrementAndGet](/classmuduo_1_1detail_1_1_atomic_integer_t.md#function-incrementandget)**() |
| [T](/classmuduo_1_1_t.md) | **[decrementAndGet](/classmuduo_1_1detail_1_1_atomic_integer_t.md#function-decrementandget)**() |
| void | **[add](/classmuduo_1_1detail_1_1_atomic_integer_t.md#function-add)**([T](/classmuduo_1_1_t.md) x) |
| void | **[increment](/classmuduo_1_1detail_1_1_atomic_integer_t.md#function-increment)**() |
| void | **[decrement](/classmuduo_1_1detail_1_1_atomic_integer_t.md#function-decrement)**() |
| [T](/classmuduo_1_1_t.md) | **[getAndSet](/classmuduo_1_1detail_1_1_atomic_integer_t.md#function-getandset)**([T](/classmuduo_1_1_t.md) newValue) |

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
class muduo::detail::AtomicIntegerT;
```

## Public Functions Documentation

### function AtomicIntegerT

```cpp
inline AtomicIntegerT()
```


### function get

```cpp
inline T get()
```


### function getAndAdd

```cpp
inline T getAndAdd(
    T x
)
```


### function addAndGet

```cpp
inline T addAndGet(
    T x
)
```


### function incrementAndGet

```cpp
inline T incrementAndGet()
```


### function decrementAndGet

```cpp
inline T decrementAndGet()
```


### function add

```cpp
inline void add(
    T x
)
```


### function increment

```cpp
inline void increment()
```


### function decrement

```cpp
inline void decrement()
```


### function getAndSet

```cpp
inline T getAndSet(
    T newValue
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800