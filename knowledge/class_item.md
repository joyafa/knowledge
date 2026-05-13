---
title: Item

---

# Item






`#include <Item.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[UpdatePolicy](/class_item.md#enum-updatepolicy)** { kInvalid, kSet, kAdd, kReplace, kAppend, kPrepend, kCas} |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| [ItemPtr](/_item_8h.md#typedef-itemptr) | **[makeItem](/class_item.md#function-makeitem)**([muduo::StringPiece](/classmuduo_1_1_string_piece.md) keyArg, uint32_t flagsArg, int exptimeArg, int valuelen, uint64_t casArg) |
| | **[Item](/class_item.md#function-item)**([muduo::StringPiece](/classmuduo_1_1_string_piece.md) keyArg, uint32_t flagsArg, int exptimeArg, int valuelen, uint64_t casArg) |
| | **[~Item](/class_item.md#function-~item)**() |
| [muduo::StringPiece](/classmuduo_1_1_string_piece.md) | **[key](/class_item.md#function-key)**() const |
| uint32_t | **[flags](/class_item.md#function-flags)**() const |
| int | **[rel_exptime](/class_item.md#function-rel-exptime)**() const |
| const char * | **[value](/class_item.md#function-value)**() const |
| size_t | **[valueLength](/class_item.md#function-valuelength)**() const |
| uint64_t | **[cas](/class_item.md#function-cas)**() const |
| size_t | **[hash](/class_item.md#function-hash)**() const |
| void | **[setCas](/class_item.md#function-setcas)**(uint64_t casArg) |
| size_t | **[neededBytes](/class_item.md#function-neededbytes)**() const |
| void | **[append](/class_item.md#function-append)**(const char * data, size_t len) |
| bool | **[endsWithCRLF](/class_item.md#function-endswithcrlf)**() const |
| void | **[output](/class_item.md#function-output)**([muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) * out, bool needCas =false) const |
| void | **[resetKey](/class_item.md#function-resetkey)**([muduo::StringPiece](/classmuduo_1_1_string_piece.md) k) |

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

### enum UpdatePolicy

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kInvalid | |   |
| kSet | |   |
| kAdd | |   |
| kReplace | |   |
| kAppend | |   |
| kPrepend | |   |
| kCas | |   |




## Public Functions Documentation

### function makeItem

```cpp
static inline ItemPtr makeItem(
    muduo::StringPiece keyArg,
    uint32_t flagsArg,
    int exptimeArg,
    int valuelen,
    uint64_t casArg
)
```


### function Item

```cpp
Item(
    muduo::StringPiece keyArg,
    uint32_t flagsArg,
    int exptimeArg,
    int valuelen,
    uint64_t casArg
)
```


### function ~Item

```cpp
inline ~Item()
```


### function key

```cpp
inline muduo::StringPiece key() const
```


### function flags

```cpp
inline uint32_t flags() const
```


### function rel_exptime

```cpp
inline int rel_exptime() const
```


### function value

```cpp
inline const char * value() const
```


### function valueLength

```cpp
inline size_t valueLength() const
```


### function cas

```cpp
inline uint64_t cas() const
```


### function hash

```cpp
inline size_t hash() const
```


### function setCas

```cpp
inline void setCas(
    uint64_t casArg
)
```


### function neededBytes

```cpp
inline size_t neededBytes() const
```


### function append

```cpp
void append(
    const char * data,
    size_t len
)
```


### function endsWithCRLF

```cpp
inline bool endsWithCRLF() const
```


### function output

```cpp
void output(
    muduo::net::Buffer * out,
    bool needCas =false
) const
```


### function resetKey

```cpp
void resetKey(
    muduo::StringPiece k
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800