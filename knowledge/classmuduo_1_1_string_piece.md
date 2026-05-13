---
title: muduo::StringPiece

---

# muduo::StringPiece






`#include <StringPiece.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[StringPiece](/classmuduo_1_1_string_piece.md#function-stringpiece)**() |
| | **[StringPiece](/classmuduo_1_1_string_piece.md#function-stringpiece)**(const char * str) |
| | **[StringPiece](/classmuduo_1_1_string_piece.md#function-stringpiece)**(const unsigned char * str) |
| | **[StringPiece](/classmuduo_1_1_string_piece.md#function-stringpiece)**(const string & str) |
| | **[StringPiece](/classmuduo_1_1_string_piece.md#function-stringpiece)**(const char * offset, int len) |
| const char * | **[data](/classmuduo_1_1_string_piece.md#function-data)**() const |
| int | **[size](/classmuduo_1_1_string_piece.md#function-size)**() const |
| bool | **[empty](/classmuduo_1_1_string_piece.md#function-empty)**() const |
| const char * | **[begin](/classmuduo_1_1_string_piece.md#function-begin)**() const |
| const char * | **[end](/classmuduo_1_1_string_piece.md#function-end)**() const |
| void | **[clear](/classmuduo_1_1_string_piece.md#function-clear)**() |
| void | **[set](/classmuduo_1_1_string_piece.md#function-set)**(const char * buffer, int len) |
| void | **[set](/classmuduo_1_1_string_piece.md#function-set)**(const char * str) |
| void | **[set](/classmuduo_1_1_string_piece.md#function-set)**(const void * buffer, int len) |
| char | **[operator[]](/classmuduo_1_1_string_piece.md#function-operator[])**(int i) const |
| void | **[remove_prefix](/classmuduo_1_1_string_piece.md#function-remove-prefix)**(int n) |
| void | **[remove_suffix](/classmuduo_1_1_string_piece.md#function-remove-suffix)**(int n) |
| bool | **[operator==](/classmuduo_1_1_string_piece.md#function-operator==)**(const [StringPiece](/classmuduo_1_1_string_piece.md#function-stringpiece) & x) const |
| bool | **[operator!=](/classmuduo_1_1_string_piece.md#function-operator!=)**(const [StringPiece](/classmuduo_1_1_string_piece.md#function-stringpiece) & x) const |
| | **[STRINGPIECE_BINARY_PREDICATE](/classmuduo_1_1_string_piece.md#function-stringpiece-binary-predicate)**() |
| | **[STRINGPIECE_BINARY_PREDICATE](/classmuduo_1_1_string_piece.md#function-stringpiece-binary-predicate)**(<= ) |
| | **[STRINGPIECE_BINARY_PREDICATE](/classmuduo_1_1_string_piece.md#function-stringpiece-binary-predicate)**(>= ) |
| | **[STRINGPIECE_BINARY_PREDICATE](/classmuduo_1_1_string_piece.md#function-stringpiece-binary-predicate)**() |
| int | **[compare](/classmuduo_1_1_string_piece.md#function-compare)**(const [StringPiece](/classmuduo_1_1_string_piece.md#function-stringpiece) & x) const |
| string | **[as_string](/classmuduo_1_1_string_piece.md#function-as-string)**() const |
| void | **[CopyToString](/classmuduo_1_1_string_piece.md#function-copytostring)**(string * target) const |
| bool | **[starts_with](/classmuduo_1_1_string_piece.md#function-starts-with)**(const [StringPiece](/classmuduo_1_1_string_piece.md#function-stringpiece) & x) const |

## Public Functions Documentation

### function StringPiece

```cpp
inline StringPiece()
```


### function StringPiece

```cpp
inline StringPiece(
    const char * str
)
```


### function StringPiece

```cpp
inline StringPiece(
    const unsigned char * str
)
```


### function StringPiece

```cpp
inline StringPiece(
    const string & str
)
```


### function StringPiece

```cpp
inline StringPiece(
    const char * offset,
    int len
)
```


### function data

```cpp
inline const char * data() const
```


### function size

```cpp
inline int size() const
```


### function empty

```cpp
inline bool empty() const
```


### function begin

```cpp
inline const char * begin() const
```


### function end

```cpp
inline const char * end() const
```


### function clear

```cpp
inline void clear()
```


### function set

```cpp
inline void set(
    const char * buffer,
    int len
)
```


### function set

```cpp
inline void set(
    const char * str
)
```


### function set

```cpp
inline void set(
    const void * buffer,
    int len
)
```


### function operator[]

```cpp
inline char operator[](
    int i
) const
```


### function remove_prefix

```cpp
inline void remove_prefix(
    int n
)
```


### function remove_suffix

```cpp
inline void remove_suffix(
    int n
)
```


### function operator==

```cpp
inline bool operator==(
    const StringPiece & x
) const
```


### function operator!=

```cpp
inline bool operator!=(
    const StringPiece & x
) const
```


### function STRINGPIECE_BINARY_PREDICATE

```cpp
STRINGPIECE_BINARY_PREDICATE()
```


### function STRINGPIECE_BINARY_PREDICATE

```cpp
STRINGPIECE_BINARY_PREDICATE(
    <= 
)
```


### function STRINGPIECE_BINARY_PREDICATE

```cpp
STRINGPIECE_BINARY_PREDICATE(
    >= 
)
```


### function STRINGPIECE_BINARY_PREDICATE

```cpp
STRINGPIECE_BINARY_PREDICATE()
```


### function compare

```cpp
inline int compare(
    const StringPiece & x
) const
```


### function as_string

```cpp
inline string as_string() const
```


### function CopyToString

```cpp
inline void CopyToString(
    string * target
) const
```


### function starts_with

```cpp
inline bool starts_with(
    const StringPiece & x
) const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800