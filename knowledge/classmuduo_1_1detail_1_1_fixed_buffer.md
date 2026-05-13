---
title: muduo::detail::FixedBuffer

---

# muduo::detail::FixedBuffer



 [More...](#detailed-description)


`#include <LogStream.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[FixedBuffer](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-fixedbuffer)**() |
| | **[~FixedBuffer](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-~fixedbuffer)**() |
| void | **[append](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-append)**(const char * buf, size_t len) |
| const char * | **[data](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-data)**() const |
| int | **[length](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-length)**() const |
| char * | **[current](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-current)**() |
| int | **[avail](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-avail)**() const |
| void | **[add](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-add)**(size_t len) |
| void | **[reset](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-reset)**() |
| void | **[bzero](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-bzero)**() |
| const char * | **[debugString](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-debugstring)**() |
| void | **[setCookie](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-setcookie)**(void(*)() cookie) |
| string | **[toString](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-tostring)**() const |
| [StringPiece](/classmuduo_1_1_string_piece.md) | **[toStringPiece](/classmuduo_1_1detail_1_1_fixed_buffer.md#function-tostringpiece)**() const |

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


## Detailed Description

```cpp
template <int SIZE>
class muduo::detail::FixedBuffer;
```

## Public Functions Documentation

### function FixedBuffer

```cpp
inline FixedBuffer()
```


### function ~FixedBuffer

```cpp
inline ~FixedBuffer()
```


### function append

```cpp
inline void append(
    const char * buf,
    size_t len
)
```


### function data

```cpp
inline const char * data() const
```


### function length

```cpp
inline int length() const
```


### function current

```cpp
inline char * current()
```


### function avail

```cpp
inline int avail() const
```


### function add

```cpp
inline void add(
    size_t len
)
```


### function reset

```cpp
inline void reset()
```


### function bzero

```cpp
inline void bzero()
```


### function debugString

```cpp
const char * debugString()
```


### function setCookie

```cpp
inline void setCookie(
    void(*)() cookie
)
```


### function toString

```cpp
inline string toString() const
```


### function toStringPiece

```cpp
inline StringPiece toStringPiece() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800