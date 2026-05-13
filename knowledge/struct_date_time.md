---
title: DateTime

---

# DateTime






`#include <TimeZone.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DateTime](/struct_date_time.md#function-datetime)**() |
| | **[DateTime](/struct_date_time.md#function-datetime)**(const struct tm & t) |
| | **[DateTime](/struct_date_time.md#function-datetime)**(int _year, int _month, int _day, int _hour, int _minute, int _second) |
| string | **[toIsoString](/struct_date_time.md#function-toisostring)**() const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[year](/struct_date_time.md#variable-year)**  |
| int | **[month](/struct_date_time.md#variable-month)**  |
| int | **[day](/struct_date_time.md#variable-day)**  |
| int | **[hour](/struct_date_time.md#variable-hour)**  |
| int | **[minute](/struct_date_time.md#variable-minute)**  |
| int | **[second](/struct_date_time.md#variable-second)**  |

## Public Functions Documentation

### function DateTime

```cpp
inline DateTime()
```


### function DateTime

```cpp
explicit DateTime(
    const struct tm & t
)
```


### function DateTime

```cpp
inline DateTime(
    int _year,
    int _month,
    int _day,
    int _hour,
    int _minute,
    int _second
)
```


### function toIsoString

```cpp
string toIsoString() const
```


## Public Attributes Documentation

### variable year

```cpp
int year = 0;
```


### variable month

```cpp
int month = 0;
```


### variable day

```cpp
int day = 0;
```


### variable hour

```cpp
int hour = 0;
```


### variable minute

```cpp
int minute = 0;
```


### variable second

```cpp
int second = 0;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800