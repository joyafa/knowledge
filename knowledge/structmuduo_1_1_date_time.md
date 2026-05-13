---
title: muduo::DateTime

---

# muduo::DateTime






`#include <TimeZone.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DateTime](/structmuduo_1_1_date_time.md#function-datetime)**() |
| | **[DateTime](/structmuduo_1_1_date_time.md#function-datetime)**(const struct tm & t) |
| | **[DateTime](/structmuduo_1_1_date_time.md#function-datetime)**(int _year, int _month, int _day, int _hour, int _minute, int _second) |
| string | **[toIsoString](/structmuduo_1_1_date_time.md#function-toisostring)**() const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[year](/structmuduo_1_1_date_time.md#variable-year)**  |
| int | **[month](/structmuduo_1_1_date_time.md#variable-month)**  |
| int | **[day](/structmuduo_1_1_date_time.md#variable-day)**  |
| int | **[hour](/structmuduo_1_1_date_time.md#variable-hour)**  |
| int | **[minute](/structmuduo_1_1_date_time.md#variable-minute)**  |
| int | **[second](/structmuduo_1_1_date_time.md#variable-second)**  |

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