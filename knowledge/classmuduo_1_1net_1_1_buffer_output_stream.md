---
title: muduo::net::BufferOutputStream

---

# muduo::net::BufferOutputStream






`#include <BufferStream.h>`

Inherits from google::protobuf::io::ZeroCopyOutputStream

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BufferOutputStream](/classmuduo_1_1net_1_1_buffer_output_stream.md#function-bufferoutputstream)**([Buffer](/class_buffer.md) * buf) |
| virtual bool | **[Next](/classmuduo_1_1net_1_1_buffer_output_stream.md#function-next)**(void ** data, int * size) |
| virtual void | **[BackUp](/classmuduo_1_1net_1_1_buffer_output_stream.md#function-backup)**(int count) |
| virtual int64_t | **[ByteCount](/classmuduo_1_1net_1_1_buffer_output_stream.md#function-bytecount)**() const |

## Public Functions Documentation

### function BufferOutputStream

```cpp
inline BufferOutputStream(
    Buffer * buf
)
```


### function Next

```cpp
inline virtual bool Next(
    void ** data,
    int * size
)
```


### function BackUp

```cpp
inline virtual void BackUp(
    int count
)
```


### function ByteCount

```cpp
inline virtual int64_t ByteCount() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800