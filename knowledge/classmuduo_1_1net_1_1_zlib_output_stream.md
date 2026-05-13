---
title: muduo::net::ZlibOutputStream

---

# muduo::net::ZlibOutputStream






`#include <ZlibStream.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ZlibOutputStream](/classmuduo_1_1net_1_1_zlib_output_stream.md#function-zliboutputstream)**([Buffer](/class_buffer.md) * output) |
| | **[~ZlibOutputStream](/classmuduo_1_1net_1_1_zlib_output_stream.md#function-~zliboutputstream)**() |
| const char * | **[zlibErrorMessage](/classmuduo_1_1net_1_1_zlib_output_stream.md#function-zliberrormessage)**() const |
| int | **[zlibErrorCode](/classmuduo_1_1net_1_1_zlib_output_stream.md#function-zliberrorcode)**() const |
| int64_t | **[inputBytes](/classmuduo_1_1net_1_1_zlib_output_stream.md#function-inputbytes)**() const |
| int64_t | **[outputBytes](/classmuduo_1_1net_1_1_zlib_output_stream.md#function-outputbytes)**() const |
| int | **[internalOutputBufferSize](/classmuduo_1_1net_1_1_zlib_output_stream.md#function-internaloutputbuffersize)**() const |
| bool | **[write](/classmuduo_1_1net_1_1_zlib_output_stream.md#function-write)**([StringPiece](/classmuduo_1_1_string_piece.md) buf) |
| bool | **[write](/classmuduo_1_1net_1_1_zlib_output_stream.md#function-write)**([Buffer](/class_buffer.md) * input) |
| bool | **[finish](/classmuduo_1_1net_1_1_zlib_output_stream.md#function-finish)**() |

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

### function ZlibOutputStream

```cpp
inline explicit ZlibOutputStream(
    Buffer * output
)
```


### function ~ZlibOutputStream

```cpp
inline ~ZlibOutputStream()
```


### function zlibErrorMessage

```cpp
inline const char * zlibErrorMessage() const
```


### function zlibErrorCode

```cpp
inline int zlibErrorCode() const
```


### function inputBytes

```cpp
inline int64_t inputBytes() const
```


### function outputBytes

```cpp
inline int64_t outputBytes() const
```


### function internalOutputBufferSize

```cpp
inline int internalOutputBufferSize() const
```


### function write

```cpp
inline bool write(
    StringPiece buf
)
```


### function write

```cpp
inline bool write(
    Buffer * input
)
```


### function finish

```cpp
inline bool finish()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800