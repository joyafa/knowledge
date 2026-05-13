---
title: muduo::ThreadPool

---

# muduo::ThreadPool






`#include <ThreadPool.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void()> | **[Task](/classmuduo_1_1_thread_pool.md#typedef-task)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ThreadPool](/classmuduo_1_1_thread_pool.md#function-threadpool)**(const string & nameArg =string("ThreadPool")) |
| | **[~ThreadPool](/classmuduo_1_1_thread_pool.md#function-~threadpool)**() |
| void | **[setMaxQueueSize](/classmuduo_1_1_thread_pool.md#function-setmaxqueuesize)**(int maxSize) |
| void | **[setThreadInitCallback](/classmuduo_1_1_thread_pool.md#function-setthreadinitcallback)**(const [Task](/classmuduo_1_1_thread_pool.md#typedef-task) & cb) |
| void | **[start](/classmuduo_1_1_thread_pool.md#function-start)**(int numThreads) |
| void | **[stop](/classmuduo_1_1_thread_pool.md#function-stop)**() |
| const string & | **[name](/classmuduo_1_1_thread_pool.md#function-name)**() const |
| size_t | **[queueSize](/classmuduo_1_1_thread_pool.md#function-queuesize)**() const |
| void | **[run](/classmuduo_1_1_thread_pool.md#function-run)**([Task](/classmuduo_1_1_thread_pool.md#typedef-task) f) |

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

### typedef Task

```cpp
typedef std::function<void ()> muduo::ThreadPool::Task;
```


## Public Functions Documentation

### function ThreadPool

```cpp
explicit ThreadPool(
    const string & nameArg =string("ThreadPool")
)
```


### function ~ThreadPool

```cpp
~ThreadPool()
```


### function setMaxQueueSize

```cpp
inline void setMaxQueueSize(
    int maxSize
)
```


### function setThreadInitCallback

```cpp
inline void setThreadInitCallback(
    const Task & cb
)
```


### function start

```cpp
void start(
    int numThreads
)
```


### function stop

```cpp
void stop()
```


### function name

```cpp
inline const string & name() const
```


### function queueSize

```cpp
size_t queueSize() const
```


### function run

```cpp
void run(
    Task f
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800