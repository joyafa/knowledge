---
title: muduo::net::ZlibInputStream

---

# muduo::net::ZlibInputStream






`#include <ZlibStream.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ZlibInputStream](/classmuduo_1_1net_1_1_zlib_input_stream.md#function-zlibinputstream)**([Buffer](/class_buffer.md) * output) |
| | **[~ZlibInputStream](/classmuduo_1_1net_1_1_zlib_input_stream.md#function-~zlibinputstream)**() |
| bool | **[write](/classmuduo_1_1net_1_1_zlib_input_stream.md#function-write)**([StringPiece](/classmuduo_1_1_string_piece.md) buf) |
| bool | **[write](/classmuduo_1_1net_1_1_zlib_input_stream.md#function-write)**([Buffer](/class_buffer.md) * input) |
| bool | **[finish](/classmuduo_1_1net_1_1_zlib_input_stream.md#function-finish)**() |

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

### function ZlibInputStream

```cpp
inline explicit ZlibInputStream(
    Buffer * output
)
```


### function ~ZlibInputStream

```cpp
inline ~ZlibInputStream()
```


### function write

```cpp
bool write(
    StringPiece buf
)
```


### function write

```cpp
bool write(
    Buffer * input
)
```


### function finish

```cpp
bool finish()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800