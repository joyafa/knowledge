---
title: muduo::Logger::SourceFile

---

# muduo::Logger::SourceFile






`#include <Logging.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| template <int N\> <br>| **[SourceFile](/classmuduo_1_1_logger_1_1_source_file.md#function-sourcefile)**(const char(&) arr[N]) |
| | **[SourceFile](/classmuduo_1_1_logger_1_1_source_file.md#function-sourcefile)**(const char * filename) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const char * | **[data_](/classmuduo_1_1_logger_1_1_source_file.md#variable-data-)**  |
| int | **[size_](/classmuduo_1_1_logger_1_1_source_file.md#variable-size-)**  |

## Public Functions Documentation

### function SourceFile

```cpp
template <int N>
inline SourceFile(
    const char(&) arr[N]
)
```


### function SourceFile

```cpp
inline explicit SourceFile(
    const char * filename
)
```


## Public Attributes Documentation

### variable data_

```cpp
const char * data_;
```


### variable size_

```cpp
int size_;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800