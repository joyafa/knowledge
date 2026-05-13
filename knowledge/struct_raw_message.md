---
title: RawMessage

---

# RawMessage





## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[RawMessage](/struct_raw_message.md#function-rawmessage)**([StringPiece](/classmuduo_1_1_string_piece.md) m) |
| uint64_t | **[id](/struct_raw_message.md#function-id)**() const |
| void | **[set_id](/struct_raw_message.md#function-set-id)**(uint64_t x) |
| bool | **[parse](/struct_raw_message.md#function-parse)**(const string & tag) |
| void | **[updateId](/struct_raw_message.md#function-updateid)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [StringPiece](/classmuduo_1_1_string_piece.md) | **[message_](/struct_raw_message.md#variable-message-)**  |

## Public Functions Documentation

### function RawMessage

```cpp
inline RawMessage(
    StringPiece m
)
```


### function id

```cpp
inline uint64_t id() const
```


### function set_id

```cpp
inline void set_id(
    uint64_t x
)
```


### function parse

```cpp
inline bool parse(
    const string & tag
)
```


### function updateId

```cpp
inline void updateId()
```


## Public Attributes Documentation

### variable message_

```cpp
StringPiece message_;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800