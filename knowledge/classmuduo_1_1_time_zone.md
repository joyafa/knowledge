---
title: muduo::TimeZone

---

# muduo::TimeZone






`#include <TimeZone.h>`

Inherits from [muduo::copyable](/classmuduo_1_1copyable.md)

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Data](/struct_time_zone_1_1_data.md)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[TimeZone](/classmuduo_1_1_time_zone.md#function-timezone)**() =default |
| | **[TimeZone](/classmuduo_1_1_time_zone.md#function-timezone)**(int eastOfUtc, const char * tzname) |
| bool | **[valid](/classmuduo_1_1_time_zone.md#function-valid)**() const |
| struct [DateTime](/struct_date_time.md) | **[toLocalTime](/classmuduo_1_1_time_zone.md#function-tolocaltime)**(int64_t secondsSinceEpoch, int * utcOffset =nullptr) const |
| int64_t | **[fromLocalTime](/classmuduo_1_1_time_zone.md#function-fromlocaltime)**(const struct [DateTime](/struct_date_time.md) & localtime, bool postTransition =false) const |
| [TimeZone](/class_time_zone.md) | **[UTC](/classmuduo_1_1_time_zone.md#function-utc)**() |
| [TimeZone](/class_time_zone.md) | **[China](/classmuduo_1_1_time_zone.md#function-china)**() |
| [TimeZone](/class_time_zone.md) | **[loadZoneFile](/classmuduo_1_1_time_zone.md#function-loadzonefile)**(const char * zonefile) |
| struct [DateTime](/struct_date_time.md) | **[toUtcTime](/classmuduo_1_1_time_zone.md#function-toutctime)**(int64_t secondsSinceEpoch) |
| int64_t | **[fromUtcTime](/classmuduo_1_1_time_zone.md#function-fromutctime)**(const struct [DateTime](/struct_date_time.md) & ) |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[TimeZoneTestPeer](/classmuduo_1_1_time_zone.md#friend-timezonetestpeer)**  |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Public Functions Documentation

### function TimeZone

```cpp
TimeZone() =default
```


### function TimeZone

```cpp
TimeZone(
    int eastOfUtc,
    const char * tzname
)
```


### function valid

```cpp
inline bool valid() const
```


### function toLocalTime

```cpp
struct DateTime toLocalTime(
    int64_t secondsSinceEpoch,
    int * utcOffset =nullptr
) const
```


### function fromLocalTime

```cpp
int64_t fromLocalTime(
    const struct DateTime & localtime,
    bool postTransition =false
) const
```


### function UTC

```cpp
static TimeZone UTC()
```


### function China

```cpp
static TimeZone China()
```


### function loadZoneFile

```cpp
static TimeZone loadZoneFile(
    const char * zonefile
)
```


### function toUtcTime

```cpp
static struct DateTime toUtcTime(
    int64_t secondsSinceEpoch
)
```


### function fromUtcTime

```cpp
static int64_t fromUtcTime(
    const struct DateTime & 
)
```


## Friends

### friend TimeZoneTestPeer

```cpp
friend class TimeZoneTestPeer(
    TimeZoneTestPeer 
);
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800