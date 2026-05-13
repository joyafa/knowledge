---
title: Buffer

---

# Buffer



 [More...](#detailed-description)


`#include <Buffer.h>`

Inherits from [muduo::copyable](/classmuduo_1_1copyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Buffer](/class_buffer.md#function-buffer)**(size_t initialSize =[kInitialSize](/class_buffer.md#variable-kinitialsize)) |
| void | **[swap](/class_buffer.md#function-swap)**([Buffer](/class_buffer.md) & rhs) |
| size_t | **[readableBytes](/class_buffer.md#function-readablebytes)**() const |
| size_t | **[writableBytes](/class_buffer.md#function-writablebytes)**() const |
| size_t | **[prependableBytes](/class_buffer.md#function-prependablebytes)**() const |
| const char * | **[peek](/class_buffer.md#function-peek)**() const |
| const char * | **[findCRLF](/class_buffer.md#function-findcrlf)**() const |
| const char * | **[findCRLF](/class_buffer.md#function-findcrlf)**(const char * start) const |
| const char * | **[findEOL](/class_buffer.md#function-findeol)**() const |
| const char * | **[findEOL](/class_buffer.md#function-findeol)**(const char * start) const |
| void | **[retrieve](/class_buffer.md#function-retrieve)**(size_t len) |
| void | **[retrieveUntil](/class_buffer.md#function-retrieveuntil)**(const char * end) |
| void | **[retrieveInt64](/class_buffer.md#function-retrieveint64)**() |
| void | **[retrieveInt32](/class_buffer.md#function-retrieveint32)**() |
| void | **[retrieveInt16](/class_buffer.md#function-retrieveint16)**() |
| void | **[retrieveInt8](/class_buffer.md#function-retrieveint8)**() |
| void | **[retrieveAll](/class_buffer.md#function-retrieveall)**() |
| string | **[retrieveAllAsString](/class_buffer.md#function-retrieveallasstring)**() |
| string | **[retrieveAsString](/class_buffer.md#function-retrieveasstring)**(size_t len) |
| StringPiece | **[toStringPiece](/class_buffer.md#function-tostringpiece)**() const |
| void | **[append](/class_buffer.md#function-append)**(const StringPiece & str) |
| void | **[append](/class_buffer.md#function-append)**(const char * data, size_t len) |
| void | **[append](/class_buffer.md#function-append)**(const void * data, size_t len) |
| void | **[ensureWritableBytes](/class_buffer.md#function-ensurewritablebytes)**(size_t len) |
| char * | **[beginWrite](/class_buffer.md#function-beginwrite)**() |
| const char * | **[beginWrite](/class_buffer.md#function-beginwrite)**() const |
| void | **[hasWritten](/class_buffer.md#function-haswritten)**(size_t len) |
| void | **[unwrite](/class_buffer.md#function-unwrite)**(size_t len) |
| void | **[appendInt64](/class_buffer.md#function-appendint64)**(int64_t x) |
| void | **[appendInt32](/class_buffer.md#function-appendint32)**(int32_t x) |
| void | **[appendInt16](/class_buffer.md#function-appendint16)**(int16_t x) |
| void | **[appendInt8](/class_buffer.md#function-appendint8)**(int8_t x) |
| int64_t | **[readInt64](/class_buffer.md#function-readint64)**() |
| int32_t | **[readInt32](/class_buffer.md#function-readint32)**() |
| int16_t | **[readInt16](/class_buffer.md#function-readint16)**() |
| int8_t | **[readInt8](/class_buffer.md#function-readint8)**() |
| int64_t | **[peekInt64](/class_buffer.md#function-peekint64)**() const |
| int32_t | **[peekInt32](/class_buffer.md#function-peekint32)**() const |
| int16_t | **[peekInt16](/class_buffer.md#function-peekint16)**() const |
| int8_t | **[peekInt8](/class_buffer.md#function-peekint8)**() const |
| void | **[prependInt64](/class_buffer.md#function-prependint64)**(int64_t x) |
| void | **[prependInt32](/class_buffer.md#function-prependint32)**(int32_t x) |
| void | **[prependInt16](/class_buffer.md#function-prependint16)**(int16_t x) |
| void | **[prependInt8](/class_buffer.md#function-prependint8)**(int8_t x) |
| void | **[prepend](/class_buffer.md#function-prepend)**(const void * data, size_t len) |
| void | **[shrink](/class_buffer.md#function-shrink)**(size_t reserve) |
| size_t | **[internalCapacity](/class_buffer.md#function-internalcapacity)**() const |
| ssize_t | **[readFd](/class_buffer.md#function-readfd)**(int fd, int * savedErrno) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const size_t | **[kCheapPrepend](/class_buffer.md#variable-kcheapprepend)**  |
| const size_t | **[kInitialSize](/class_buffer.md#variable-kinitialsize)**  |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Detailed Description

```cpp
class Buffer;
```


A buffer class modeled after org.jboss.netty.buffer.ChannelBuffer



```cpp
+-------------------+------------------+------------------+
| prependable bytes |  readable bytes  |  writable bytes  |
|                   |     (CONTENT)    |                  |
+-------------------+------------------+------------------+
|                   |                  |                  |
0      <=      readerIndex   <=   writerIndex    <=     size
```

## Public Functions Documentation

### function Buffer

```cpp
inline explicit Buffer(
    size_t initialSize =kInitialSize
)
```


### function swap

```cpp
inline void swap(
    Buffer & rhs
)
```


### function readableBytes

```cpp
inline size_t readableBytes() const
```


### function writableBytes

```cpp
inline size_t writableBytes() const
```


### function prependableBytes

```cpp
inline size_t prependableBytes() const
```


### function peek

```cpp
inline const char * peek() const
```


### function findCRLF

```cpp
inline const char * findCRLF() const
```


### function findCRLF

```cpp
inline const char * findCRLF(
    const char * start
) const
```


### function findEOL

```cpp
inline const char * findEOL() const
```


### function findEOL

```cpp
inline const char * findEOL(
    const char * start
) const
```


### function retrieve

```cpp
inline void retrieve(
    size_t len
)
```


### function retrieveUntil

```cpp
inline void retrieveUntil(
    const char * end
)
```


### function retrieveInt64

```cpp
inline void retrieveInt64()
```


### function retrieveInt32

```cpp
inline void retrieveInt32()
```


### function retrieveInt16

```cpp
inline void retrieveInt16()
```


### function retrieveInt8

```cpp
inline void retrieveInt8()
```


### function retrieveAll

```cpp
inline void retrieveAll()
```


### function retrieveAllAsString

```cpp
inline string retrieveAllAsString()
```


### function retrieveAsString

```cpp
inline string retrieveAsString(
    size_t len
)
```


### function toStringPiece

```cpp
inline StringPiece toStringPiece() const
```


### function append

```cpp
inline void append(
    const StringPiece & str
)
```


### function append

```cpp
inline void append(
    const char * data,
    size_t len
)
```


### function append

```cpp
inline void append(
    const void * data,
    size_t len
)
```


### function ensureWritableBytes

```cpp
inline void ensureWritableBytes(
    size_t len
)
```


### function beginWrite

```cpp
inline char * beginWrite()
```


### function beginWrite

```cpp
inline const char * beginWrite() const
```


### function hasWritten

```cpp
inline void hasWritten(
    size_t len
)
```


### function unwrite

```cpp
inline void unwrite(
    size_t len
)
```


### function appendInt64

```cpp
inline void appendInt64(
    int64_t x
)
```


Append int64_t using network endian 


### function appendInt32

```cpp
inline void appendInt32(
    int32_t x
)
```


Append int32_t using network endian 


### function appendInt16

```cpp
inline void appendInt16(
    int16_t x
)
```


### function appendInt8

```cpp
inline void appendInt8(
    int8_t x
)
```


### function readInt64

```cpp
inline int64_t readInt64()
```


Read int64_t from network endian

Require: buf->[readableBytes()](/class_buffer.md#function-readablebytes) >= sizeof(int32_t) 


### function readInt32

```cpp
inline int32_t readInt32()
```


Read int32_t from network endian

Require: buf->[readableBytes()](/class_buffer.md#function-readablebytes) >= sizeof(int32_t) 


### function readInt16

```cpp
inline int16_t readInt16()
```


### function readInt8

```cpp
inline int8_t readInt8()
```


### function peekInt64

```cpp
inline int64_t peekInt64() const
```


Peek int64_t from network endian

Require: buf->[readableBytes()](/class_buffer.md#function-readablebytes) >= sizeof(int64_t) 


### function peekInt32

```cpp
inline int32_t peekInt32() const
```


Peek int32_t from network endian

Require: buf->[readableBytes()](/class_buffer.md#function-readablebytes) >= sizeof(int32_t) 


### function peekInt16

```cpp
inline int16_t peekInt16() const
```


### function peekInt8

```cpp
inline int8_t peekInt8() const
```


### function prependInt64

```cpp
inline void prependInt64(
    int64_t x
)
```


Prepend int64_t using network endian 


### function prependInt32

```cpp
inline void prependInt32(
    int32_t x
)
```


Prepend int32_t using network endian 


### function prependInt16

```cpp
inline void prependInt16(
    int16_t x
)
```


### function prependInt8

```cpp
inline void prependInt8(
    int8_t x
)
```


### function prepend

```cpp
inline void prepend(
    const void * data,
    size_t len
)
```


### function shrink

```cpp
inline void shrink(
    size_t reserve
)
```


### function internalCapacity

```cpp
inline size_t internalCapacity() const
```


### function readFd

```cpp
ssize_t readFd(
    int fd,
    int * savedErrno
)
```


**Return**: result of read(2), `errno` is saved 

Read data directly into buffer.

It may implement with readv(2) 


## Public Attributes Documentation

### variable kCheapPrepend

```cpp
static const size_t kCheapPrepend = 8;
```


### variable kInitialSize

```cpp
static const size_t kInitialSize = 1024;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800