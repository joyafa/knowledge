---
title: muduo::ThreadLocalSingleton::Deleter

---

# muduo::ThreadLocalSingleton::Deleter





## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Deleter](/classmuduo_1_1_thread_local_singleton_1_1_deleter.md#function-deleter)**() |
| | **[~Deleter](/classmuduo_1_1_thread_local_singleton_1_1_deleter.md#function-~deleter)**() |
| void | **[set](/classmuduo_1_1_thread_local_singleton_1_1_deleter.md#function-set)**([T](/classmuduo_1_1_t.md) * newObj) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| pthread_key_t | **[pkey_](/classmuduo_1_1_thread_local_singleton_1_1_deleter.md#variable-pkey-)**  |

## Public Functions Documentation

### function Deleter

```cpp
inline Deleter()
```


### function ~Deleter

```cpp
inline ~Deleter()
```


### function set

```cpp
inline void set(
    T * newObj
)
```


## Public Attributes Documentation

### variable pkey_

```cpp
pthread_key_t pkey_;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800