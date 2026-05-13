---
title: muduo::LogStream

---

# muduo::LogStream






`#include <LogStream.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [detail::FixedBuffer](/classmuduo_1_1detail_1_1_fixed_buffer.md)< [detail::kSmallBuffer](/namespacemuduo_1_1detail.md#variable-ksmallbuffer) > | **[Buffer](/classmuduo_1_1_log_stream.md#typedef-buffer)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(bool v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(short v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(unsigned short v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(int v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(unsigned int v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(long v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(unsigned long v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(long long v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(unsigned long long v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(const void * p) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(float v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(double v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(char v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(const char * str) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(const unsigned char * str) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(const string & v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(const [StringPiece](/classmuduo_1_1_string_piece.md) & v) |
| self & | **[operator<<](/classmuduo_1_1_log_stream.md#function-operator<<)**(const [Buffer](/classmuduo_1_1_log_stream.md#typedef-buffer) & v) |
| void | **[append](/classmuduo_1_1_log_stream.md#function-append)**(const char * data, int len) |
| const [Buffer](/classmuduo_1_1_log_stream.md#typedef-buffer) & | **[buffer](/classmuduo_1_1_log_stream.md#function-buffer)**() const |
| void | **[resetBuffer](/classmuduo_1_1_log_stream.md#function-resetbuffer)**() |

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


## Public Types Documentation

### typedef Buffer

```cpp
typedef detail::FixedBuffer<detail::kSmallBuffer> muduo::LogStream::Buffer;
```


## Public Functions Documentation

### function operator<<

```cpp
inline self & operator<<(
    bool v
)
```


### function operator<<

```cpp
self & operator<<(
    short v
)
```


### function operator<<

```cpp
self & operator<<(
    unsigned short v
)
```


### function operator<<

```cpp
self & operator<<(
    int v
)
```


### function operator<<

```cpp
self & operator<<(
    unsigned int v
)
```


### function operator<<

```cpp
self & operator<<(
    long v
)
```


### function operator<<

```cpp
self & operator<<(
    unsigned long v
)
```


### function operator<<

```cpp
self & operator<<(
    long long v
)
```


### function operator<<

```cpp
self & operator<<(
    unsigned long long v
)
```


### function operator<<

```cpp
self & operator<<(
    const void * p
)
```


### function operator<<

```cpp
inline self & operator<<(
    float v
)
```


### function operator<<

```cpp
self & operator<<(
    double v
)
```


### function operator<<

```cpp
inline self & operator<<(
    char v
)
```


### function operator<<

```cpp
inline self & operator<<(
    const char * str
)
```


### function operator<<

```cpp
inline self & operator<<(
    const unsigned char * str
)
```


### function operator<<

```cpp
inline self & operator<<(
    const string & v
)
```


### function operator<<

```cpp
inline self & operator<<(
    const StringPiece & v
)
```


### function operator<<

```cpp
inline self & operator<<(
    const Buffer & v
)
```


### function append

```cpp
inline void append(
    const char * data,
    int len
)
```


### function buffer

```cpp
inline const Buffer & buffer() const
```


### function resetBuffer

```cpp
inline void resetBuffer()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800