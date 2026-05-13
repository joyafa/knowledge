---
title: muduo::detail::ThreadData

---

# muduo::detail::ThreadData





## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [muduo::Thread::ThreadFunc](/classmuduo_1_1_thread.md#typedef-threadfunc) | **[ThreadFunc](/structmuduo_1_1detail_1_1_thread_data.md#typedef-threadfunc)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ThreadData](/structmuduo_1_1detail_1_1_thread_data.md#function-threaddata)**([ThreadFunc](/structmuduo_1_1detail_1_1_thread_data.md#typedef-threadfunc) func, const string & name, pid_t * tid, [CountDownLatch](/classmuduo_1_1_count_down_latch.md) * latch) |
| void | **[runInThread](/structmuduo_1_1detail_1_1_thread_data.md#function-runinthread)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [ThreadFunc](/structmuduo_1_1detail_1_1_thread_data.md#typedef-threadfunc) | **[func_](/structmuduo_1_1detail_1_1_thread_data.md#variable-func-)**  |
| string | **[name_](/structmuduo_1_1detail_1_1_thread_data.md#variable-name-)**  |
| pid_t * | **[tid_](/structmuduo_1_1detail_1_1_thread_data.md#variable-tid-)**  |
| [CountDownLatch](/classmuduo_1_1_count_down_latch.md) * | **[latch_](/structmuduo_1_1detail_1_1_thread_data.md#variable-latch-)**  |

## Public Types Documentation

### typedef ThreadFunc

```cpp
typedef muduo::Thread::ThreadFunc muduo::detail::ThreadData::ThreadFunc;
```


## Public Functions Documentation

### function ThreadData

```cpp
inline ThreadData(
    ThreadFunc func,
    const string & name,
    pid_t * tid,
    CountDownLatch * latch
)
```


### function runInThread

```cpp
inline void runInThread()
```


## Public Attributes Documentation

### variable func_

```cpp
ThreadFunc func_;
```


### variable name_

```cpp
string name_;
```


### variable tid_

```cpp
pid_t * tid_;
```


### variable latch_

```cpp
CountDownLatch * latch_;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800