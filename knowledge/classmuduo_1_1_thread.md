---
title: muduo::Thread

---

# muduo::Thread






`#include <Thread.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void()> | **[ThreadFunc](/classmuduo_1_1_thread.md#typedef-threadfunc)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Thread](/classmuduo_1_1_thread.md#function-thread)**([ThreadFunc](/classmuduo_1_1_thread.md#typedef-threadfunc) func, const string & name =string()) |
| | **[~Thread](/classmuduo_1_1_thread.md#function-~thread)**() |
| void | **[start](/classmuduo_1_1_thread.md#function-start)**() |
| int | **[join](/classmuduo_1_1_thread.md#function-join)**() |
| bool | **[started](/classmuduo_1_1_thread.md#function-started)**() const |
| pid_t | **[tid](/classmuduo_1_1_thread.md#function-tid)**() const |
| const string & | **[name](/classmuduo_1_1_thread.md#function-name)**() const |
| int | **[numCreated](/classmuduo_1_1_thread.md#function-numcreated)**() |

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


## Public Types Documentation

### typedef ThreadFunc

```cpp
typedef std::function<void ()> muduo::Thread::ThreadFunc;
```


## Public Functions Documentation

### function Thread

```cpp
explicit Thread(
    ThreadFunc func,
    const string & name =string()
)
```


### function ~Thread

```cpp
~Thread()
```


### function start

```cpp
void start()
```


### function join

```cpp
int join()
```


### function started

```cpp
inline bool started() const
```


### function tid

```cpp
inline pid_t tid() const
```


### function name

```cpp
inline const string & name() const
```


### function numCreated

```cpp
static inline int numCreated()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800