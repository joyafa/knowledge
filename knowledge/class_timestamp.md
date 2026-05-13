---
title: Timestamp

---

# Timestamp



 [More...](#detailed-description)


`#include <Timestamp.h>`

Inherits from [muduo::copyable](/classmuduo_1_1copyable.md), boost::equality_comparable< Timestamp >, boost::less_than_comparable< Timestamp >

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Timestamp](/class_timestamp.md#function-timestamp)**() |
| | **[Timestamp](/class_timestamp.md#function-timestamp)**(int64_t microSecondsSinceEpochArg) |
| void | **[swap](/class_timestamp.md#function-swap)**([Timestamp](/class_timestamp.md) & that) |
| string | **[toString](/class_timestamp.md#function-tostring)**() const |
| string | **[toFormattedString](/class_timestamp.md#function-toformattedstring)**(bool showMicroseconds =true) const |
| bool | **[valid](/class_timestamp.md#function-valid)**() const |
| int64_t | **[microSecondsSinceEpoch](/class_timestamp.md#function-microsecondssinceepoch)**() const |
| time_t | **[secondsSinceEpoch](/class_timestamp.md#function-secondssinceepoch)**() const |
| [Timestamp](/class_timestamp.md) | **[now](/class_timestamp.md#function-now)**() |
| [Timestamp](/class_timestamp.md) | **[invalid](/class_timestamp.md#function-invalid)**() |
| [Timestamp](/class_timestamp.md) | **[fromUnixTime](/class_timestamp.md#function-fromunixtime)**(time_t t) |
| [Timestamp](/class_timestamp.md) | **[fromUnixTime](/class_timestamp.md#function-fromunixtime)**(time_t t, int microseconds) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const int | **[kMicroSecondsPerSecond](/class_timestamp.md#variable-kmicrosecondspersecond)**  |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Detailed Description

```cpp
class Timestamp;
```


Time stamp in UTC, in microseconds resolution.

This class is immutable. It's recommended to pass it by value, since it's passed in register on x64. 

## Public Functions Documentation

### function Timestamp

```cpp
inline Timestamp()
```


Constucts an invalid [Timestamp](/class_timestamp.md). 


### function Timestamp

```cpp
inline explicit Timestamp(
    int64_t microSecondsSinceEpochArg
)
```


**Parameters**: 

  * **microSecondsSinceEpoch** 


Constucts a [Timestamp](/class_timestamp.md) at specific time


### function swap

```cpp
inline void swap(
    Timestamp & that
)
```


### function toString

```cpp
string toString() const
```


### function toFormattedString

```cpp
string toFormattedString(
    bool showMicroseconds =true
) const
```


### function valid

```cpp
inline bool valid() const
```


### function microSecondsSinceEpoch

```cpp
inline int64_t microSecondsSinceEpoch() const
```


### function secondsSinceEpoch

```cpp
inline time_t secondsSinceEpoch() const
```


### function now

```cpp
static Timestamp now()
```


Get time of now. 


### function invalid

```cpp
static inline Timestamp invalid()
```


### function fromUnixTime

```cpp
static inline Timestamp fromUnixTime(
    time_t t
)
```


### function fromUnixTime

```cpp
static inline Timestamp fromUnixTime(
    time_t t,
    int microseconds
)
```


## Public Attributes Documentation

### variable kMicroSecondsPerSecond

```cpp
static const int kMicroSecondsPerSecond = 1000 * 1000;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800