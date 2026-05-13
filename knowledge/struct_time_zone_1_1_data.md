---
title: TimeZone::Data

---

# TimeZone::Data





## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Transition](/struct_time_zone_1_1_data_1_1_transition.md)**  |
| struct | **[LocalTime](/struct_time_zone_1_1_data_1_1_local_time.md)**  |
| struct | **[CompareUtcTime](/struct_time_zone_1_1_data_1_1_compare_utc_time.md)**  |
| struct | **[CompareLocalTime](/struct_time_zone_1_1_data_1_1_compare_local_time.md)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[addLocalTime](/struct_time_zone_1_1_data.md#function-addlocaltime)**(int32_t utcOffset, bool isDst, int desigIdx) |
| void | **[addTransition](/struct_time_zone_1_1_data.md#function-addtransition)**(int64_t utcTime, int localtimeIdx) |
| const [LocalTime](/struct_time_zone_1_1_data_1_1_local_time.md) * | **[findLocalTime](/struct_time_zone_1_1_data.md#function-findlocaltime)**(int64_t utcTime) const |
| const [LocalTime](/struct_time_zone_1_1_data_1_1_local_time.md) * | **[findLocalTime](/struct_time_zone_1_1_data.md#function-findlocaltime)**(const struct [DateTime](/struct_date_time.md) & local, bool postTransition) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< [Transition](/struct_time_zone_1_1_data_1_1_transition.md) > | **[transitions](/struct_time_zone_1_1_data.md#variable-transitions)**  |
| std::vector< [LocalTime](/struct_time_zone_1_1_data_1_1_local_time.md) > | **[localtimes](/struct_time_zone_1_1_data.md#variable-localtimes)**  |
| string | **[abbreviation](/struct_time_zone_1_1_data.md#variable-abbreviation)**  |
| string | **[tzstring](/struct_time_zone_1_1_data.md#variable-tzstring)**  |

## Public Functions Documentation

### function addLocalTime

```cpp
inline void addLocalTime(
    int32_t utcOffset,
    bool isDst,
    int desigIdx
)
```


### function addTransition

```cpp
inline void addTransition(
    int64_t utcTime,
    int localtimeIdx
)
```


### function findLocalTime

```cpp
const LocalTime * findLocalTime(
    int64_t utcTime
) const
```


### function findLocalTime

```cpp
const LocalTime * findLocalTime(
    const struct DateTime & local,
    bool postTransition
) const
```


## Public Attributes Documentation

### variable transitions

```cpp
std::vector< Transition > transitions;
```


### variable localtimes

```cpp
std::vector< LocalTime > localtimes;
```


### variable abbreviation

```cpp
string abbreviation;
```


### variable tzstring

```cpp
string tzstring;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800