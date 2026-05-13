---
title: muduo::FileUtil::ReadSmallFile

---

# muduo::FileUtil::ReadSmallFile






`#include <FileUtil.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ReadSmallFile](/classmuduo_1_1_file_util_1_1_read_small_file.md#function-readsmallfile)**([StringArg](/classmuduo_1_1_string_arg.md) filename) |
| | **[~ReadSmallFile](/classmuduo_1_1_file_util_1_1_read_small_file.md#function-~readsmallfile)**() |
| template <typename String \> <br>int | **[readToString](/classmuduo_1_1_file_util_1_1_read_small_file.md#function-readtostring)**(int maxSize, String * content, int64_t * fileSize, int64_t * modifyTime, int64_t * createTime) |
| int | **[readToBuffer](/classmuduo_1_1_file_util_1_1_read_small_file.md#function-readtobuffer)**(int * size)<br>Read at maxium kBufferSize into buf_.  |
| const char * | **[buffer](/classmuduo_1_1_file_util_1_1_read_small_file.md#function-buffer)**() const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const int | **[kBufferSize](/classmuduo_1_1_file_util_1_1_read_small_file.md#variable-kbuffersize)**  |

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


## Public Functions Documentation

### function ReadSmallFile

```cpp
ReadSmallFile(
    StringArg filename
)
```


### function ~ReadSmallFile

```cpp
~ReadSmallFile()
```


### function readToString

```cpp
template <typename String >
int readToString(
    int maxSize,
    String * content,
    int64_t * fileSize,
    int64_t * modifyTime,
    int64_t * createTime
)
```


### function readToBuffer

```cpp
int readToBuffer(
    int * size
)
```

Read at maxium kBufferSize into buf_. 

### function buffer

```cpp
inline const char * buffer() const
```


## Public Attributes Documentation

### variable kBufferSize

```cpp
static const int kBufferSize = 64*1024;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800