---
title: muduo::GzipFile

---

# muduo::GzipFile






`#include <GzipFile.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[GzipFile](/classmuduo_1_1_gzip_file.md#function-gzipfile)**(GzipFile && rhs) |
| | **[~GzipFile](/classmuduo_1_1_gzip_file.md#function-~gzipfile)**() |
| [GzipFile](/classmuduo_1_1_gzip_file.md#function-gzipfile) & | **[operator=](/classmuduo_1_1_gzip_file.md#function-operator=)**([GzipFile](/classmuduo_1_1_gzip_file.md#function-gzipfile) && rhs) |
| bool | **[valid](/classmuduo_1_1_gzip_file.md#function-valid)**() const |
| void | **[swap](/classmuduo_1_1_gzip_file.md#function-swap)**([GzipFile](/classmuduo_1_1_gzip_file.md#function-gzipfile) & rhs) |
| int | **[read](/classmuduo_1_1_gzip_file.md#function-read)**(void * buf, int len) |
| int | **[write](/classmuduo_1_1_gzip_file.md#function-write)**([StringPiece](/classmuduo_1_1_string_piece.md) buf) |
| off_t | **[tell](/classmuduo_1_1_gzip_file.md#function-tell)**() const |
| [GzipFile](/classmuduo_1_1_gzip_file.md#function-gzipfile) | **[openForRead](/classmuduo_1_1_gzip_file.md#function-openforread)**([StringArg](/classmuduo_1_1_string_arg.md) filename) |
| [GzipFile](/classmuduo_1_1_gzip_file.md#function-gzipfile) | **[openForAppend](/classmuduo_1_1_gzip_file.md#function-openforappend)**([StringArg](/classmuduo_1_1_string_arg.md) filename) |
| [GzipFile](/classmuduo_1_1_gzip_file.md#function-gzipfile) | **[openForWriteExclusive](/classmuduo_1_1_gzip_file.md#function-openforwriteexclusive)**([StringArg](/classmuduo_1_1_string_arg.md) filename) |
| [GzipFile](/classmuduo_1_1_gzip_file.md#function-gzipfile) | **[openForWriteTruncate](/classmuduo_1_1_gzip_file.md#function-openforwritetruncate)**([StringArg](/classmuduo_1_1_string_arg.md) filename) |

## Additional inherited members

**Public Functions inherited from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**(const noncopyable & ) =delete |

**Protected Functions inherited from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**() =default |
| | **[~noncopyable](/classmuduo_1_1noncopyable.md#function-~noncopyable)**() =default |


## Public Functions Documentation

### function GzipFile

```cpp
inline GzipFile(
    GzipFile && rhs
)
```


### function ~GzipFile

```cpp
inline ~GzipFile()
```


### function operator=

```cpp
inline GzipFile & operator=(
    GzipFile && rhs
)
```


### function valid

```cpp
inline bool valid() const
```


### function swap

```cpp
inline void swap(
    GzipFile & rhs
)
```


### function read

```cpp
inline int read(
    void * buf,
    int len
)
```


### function write

```cpp
inline int write(
    StringPiece buf
)
```


### function tell

```cpp
inline off_t tell() const
```


### function openForRead

```cpp
static inline GzipFile openForRead(
    StringArg filename
)
```


### function openForAppend

```cpp
static inline GzipFile openForAppend(
    StringArg filename
)
```


### function openForWriteExclusive

```cpp
static inline GzipFile openForWriteExclusive(
    StringArg filename
)
```


### function openForWriteTruncate

```cpp
static inline GzipFile openForWriteTruncate(
    StringArg filename
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800