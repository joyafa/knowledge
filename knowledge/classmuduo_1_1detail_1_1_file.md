---
title: muduo::detail::File

---

# muduo::detail::File





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[File](/classmuduo_1_1detail_1_1_file.md#function-file)**(const char * file) |
| | **[~File](/classmuduo_1_1detail_1_1_file.md#function-~file)**() |
| bool | **[valid](/classmuduo_1_1detail_1_1_file.md#function-valid)**() const |
| string | **[readBytes](/classmuduo_1_1detail_1_1_file.md#function-readbytes)**(int n) |
| string | **[readToEnd](/classmuduo_1_1detail_1_1_file.md#function-readtoend)**() |
| int64_t | **[readInt64](/classmuduo_1_1detail_1_1_file.md#function-readint64)**() |
| int32_t | **[readInt32](/classmuduo_1_1detail_1_1_file.md#function-readint32)**() |
| uint8_t | **[readUInt8](/classmuduo_1_1detail_1_1_file.md#function-readuint8)**() |
| off_t | **[skip](/classmuduo_1_1detail_1_1_file.md#function-skip)**(ssize_t bytes) |

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

### function File

```cpp
inline File(
    const char * file
)
```


### function ~File

```cpp
inline ~File()
```


### function valid

```cpp
inline bool valid() const
```


### function readBytes

```cpp
inline string readBytes(
    int n
)
```


### function readToEnd

```cpp
inline string readToEnd()
```


### function readInt64

```cpp
inline int64_t readInt64()
```


### function readInt32

```cpp
inline int32_t readInt32()
```


### function readUInt8

```cpp
inline uint8_t readUInt8()
```


### function skip

```cpp
inline off_t skip(
    ssize_t bytes
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800