---
title: Date

---

# Date



 [More...](#detailed-description)


`#include <Date.h>`

Inherits from [muduo::copyable](/classmuduo_1_1copyable.md)

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[YearMonthDay](/struct_date_1_1_year_month_day.md)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Date](/class_date.md#function-date)**() |
| | **[Date](/class_date.md#function-date)**(int year, int month, int day) |
| | **[Date](/class_date.md#function-date)**(int julianDayNum) |
| | **[Date](/class_date.md#function-date)**(const struct tm & t) |
| void | **[swap](/class_date.md#function-swap)**([Date](/class_date.md) & that) |
| bool | **[valid](/class_date.md#function-valid)**() const |
| string | **[toIsoString](/class_date.md#function-toisostring)**() const |
| struct [YearMonthDay](/struct_date_1_1_year_month_day.md) | **[yearMonthDay](/class_date.md#function-yearmonthday)**() const |
| int | **[year](/class_date.md#function-year)**() const |
| int | **[month](/class_date.md#function-month)**() const |
| int | **[day](/class_date.md#function-day)**() const |
| int | **[weekDay](/class_date.md#function-weekday)**() const |
| int | **[julianDayNumber](/class_date.md#function-juliandaynumber)**() const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const int | **[kDaysPerWeek](/class_date.md#variable-kdaysperweek)**  |
| const int | **[kJulianDayOf1970_01_01](/class_date.md#variable-kjuliandayof1970-01-01)**  |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Detailed Description

```cpp
class Date;
```


[Date](/class_date.md) in Gregorian calendar.

This class is immutable. It's recommended to pass it by value, since it's passed in register on x64. 

## Public Functions Documentation

### function Date

```cpp
inline Date()
```


Constucts an invalid [Date](/class_date.md). 


### function Date

```cpp
Date(
    int year,
    int month,
    int day
)
```


Constucts a yyyy-mm-dd [Date](/class_date.md).

1 <= month <= 12 


### function Date

```cpp
inline explicit Date(
    int julianDayNum
)
```


Constucts a [Date](/class_date.md) from Julian Day Number. 


### function Date

```cpp
explicit Date(
    const struct tm & t
)
```


Constucts a [Date](/class_date.md) from struct tm 


### function swap

```cpp
inline void swap(
    Date & that
)
```


### function valid

```cpp
inline bool valid() const
```


### function toIsoString

```cpp
string toIsoString() const
```


Converts to yyyy-mm-dd format. 


### function yearMonthDay

```cpp
struct YearMonthDay yearMonthDay() const
```


### function year

```cpp
inline int year() const
```


### function month

```cpp
inline int month() const
```


### function day

```cpp
inline int day() const
```


### function weekDay

```cpp
inline int weekDay() const
```


### function julianDayNumber

```cpp
inline int julianDayNumber() const
```


## Public Attributes Documentation

### variable kDaysPerWeek

```cpp
static const int kDaysPerWeek = 7;
```


### variable kJulianDayOf1970_01_01

```cpp
static const int kJulianDayOf1970_01_01 = detail::getJulianDayNumber(1970, 1, 1);
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800