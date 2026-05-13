---
title: muduo::FileUtil::AppendFile

---

# muduo::FileUtil::AppendFile






`#include <FileUtil.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[AppendFile](/classmuduo_1_1_file_util_1_1_append_file.md#function-appendfile)**([StringArg](/classmuduo_1_1_string_arg.md) filename) |
| | **[~AppendFile](/classmuduo_1_1_file_util_1_1_append_file.md#function-~appendfile)**() |
| void | **[append](/classmuduo_1_1_file_util_1_1_append_file.md#function-append)**(const char * logline, size_t len) |
| void | **[flush](/classmuduo_1_1_file_util_1_1_append_file.md#function-flush)**() |
| off_t | **[writtenBytes](/classmuduo_1_1_file_util_1_1_append_file.md#function-writtenbytes)**() const |

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

### function AppendFile

```cpp
explicit AppendFile(
    StringArg filename
)
```


### function ~AppendFile

```cpp
~AppendFile()
```


### function append

```cpp
void append(
    const char * logline,
    size_t len
)
```


### function flush

```cpp
void flush()
```


### function writtenBytes

```cpp
inline off_t writtenBytes() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800