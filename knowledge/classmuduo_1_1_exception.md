---
title: muduo::Exception

---

# muduo::Exception






`#include <Exception.h>`

Inherits from std::exception

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Exception](/classmuduo_1_1_exception.md#function-exception)**(string what) |
| | **[~Exception](/classmuduo_1_1_exception.md#function-~exception)**() override =default |
| const char * | **[what](/classmuduo_1_1_exception.md#function-what)**() const override |
| const char * | **[stackTrace](/classmuduo_1_1_exception.md#function-stacktrace)**() const |

## Public Functions Documentation

### function Exception

```cpp
Exception(
    string what
)
```


### function ~Exception

```cpp
~Exception() override =default
```


### function what

```cpp
inline const char * what() const override
```


### function stackTrace

```cpp
inline const char * stackTrace() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800