---
title: muduo::detail

---

# muduo::detail



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::detail::AtomicIntegerT](/classmuduo_1_1detail_1_1_atomic_integer_t.md)**  |
| class | **[muduo::detail::File](/classmuduo_1_1detail_1_1_file.md)**  |
| class | **[muduo::detail::FixedBuffer](/classmuduo_1_1detail_1_1_fixed_buffer.md)**  |
| struct | **[muduo::detail::has_no_destroy](/structmuduo_1_1detail_1_1has__no__destroy.md)**  |
| struct | **[muduo::detail::ThreadData](/structmuduo_1_1detail_1_1_thread_data.md)**  |
| class | **[muduo::detail::ThreadNameInitializer](/classmuduo_1_1detail_1_1_thread_name_initializer.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[getJulianDayNumber](/namespacemuduo_1_1detail.md#function-getjuliandaynumber)**(int year, int month, int day) |
| struct [Date::YearMonthDay](/struct_date_1_1_year_month_day.md) | **[getYearMonthDay](/namespacemuduo_1_1detail.md#function-getyearmonthday)**(int julianDayNumber) |
| template <typename T \> <br>size_t | **[convert](/namespacemuduo_1_1detail.md#function-convert)**(char buf[], [T](/classmuduo_1_1_t.md) value) |
| size_t | **[convertHex](/namespacemuduo_1_1detail.md#function-converthex)**(char buf[], uintptr_t value) |
| int | **[fdDirFilter](/namespacemuduo_1_1detail.md#function-fddirfilter)**(const struct dirent * d) |
| int | **[taskDirFilter](/namespacemuduo_1_1detail.md#function-taskdirfilter)**(const struct dirent * d) |
| int | **[scanDir](/namespacemuduo_1_1detail.md#function-scandir)**(const char * dirpath, int(*)(const struct dirent *) filter) |
| pid_t | **[gettid](/namespacemuduo_1_1detail.md#function-gettid)**() |
| void | **[afterFork](/namespacemuduo_1_1detail.md#function-afterfork)**() |
| void * | **[startThread](/namespacemuduo_1_1detail.md#function-startthread)**(void * obj) |
| bool | **[readDataBlock](/namespacemuduo_1_1detail.md#function-readdatablock)**([File](/classmuduo_1_1detail_1_1_file.md) & f, struct [TimeZone::Data](/struct_time_zone_1_1_data.md) * data, bool v1) |
| bool | **[readTimeZoneFile](/namespacemuduo_1_1detail.md#function-readtimezonefile)**(const char * zonefile, struct [TimeZone::Data](/struct_time_zone_1_1_data.md) * data) |
| void | **[fillHMS](/namespacemuduo_1_1detail.md#function-fillhms)**(unsigned seconds, struct [DateTime](/struct_date_time.md) * dt) |
| [DateTime](/struct_date_time.md) | **[BreakTime](/namespacemuduo_1_1detail.md#function-breaktime)**(int64_t t) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| char[sizeof(int) >=sizeof(int32_t) ? 1 :-1] | **[require_32_bit_integer_at_least](/namespacemuduo_1_1detail.md#variable-require-32-bit-integer-at-least)**  |
| const char[] | **[digits](/namespacemuduo_1_1detail.md#variable-digits)**  |
| const char * | **[zero](/namespacemuduo_1_1detail.md#variable-zero)**  |
| const char[] | **[digitsHex](/namespacemuduo_1_1detail.md#variable-digitshex)**  |
| const int | **[kSmallBuffer](/namespacemuduo_1_1detail.md#variable-ksmallbuffer)**  |
| const int | **[kLargeBuffer](/namespacemuduo_1_1detail.md#variable-klargebuffer)**  |
| __thread int | **[t_numOpenedFiles](/namespacemuduo_1_1detail.md#variable-t-numopenedfiles)**  |
| __thread std::vector< pid_t > * | **[t_pids](/namespacemuduo_1_1detail.md#variable-t-pids)**  |
| [Timestamp](/class_timestamp.md) | **[g_startTime](/namespacemuduo_1_1detail.md#variable-g-starttime)**  |
| int | **[g_clockTicks](/namespacemuduo_1_1detail.md#variable-g-clockticks)**  |
| int | **[g_pageSize](/namespacemuduo_1_1detail.md#variable-g-pagesize)**  |
| [ThreadNameInitializer](/classmuduo_1_1detail_1_1_thread_name_initializer.md) | **[init](/namespacemuduo_1_1detail.md#variable-init)**  |


## Functions Documentation

### function getJulianDayNumber

```cpp
int getJulianDayNumber(
    int year,
    int month,
    int day
)
```


### function getYearMonthDay

```cpp
struct Date::YearMonthDay getYearMonthDay(
    int julianDayNumber
)
```


### function convert

```cpp
template <typename T >
size_t convert(
    char buf[],
    T value
)
```


### function convertHex

```cpp
size_t convertHex(
    char buf[],
    uintptr_t value
)
```


### function fdDirFilter

```cpp
int fdDirFilter(
    const struct dirent * d
)
```


### function taskDirFilter

```cpp
int taskDirFilter(
    const struct dirent * d
)
```


### function scanDir

```cpp
int scanDir(
    const char * dirpath,
    int(*)(const struct dirent *) filter
)
```


### function gettid

```cpp
pid_t gettid()
```


### function afterFork

```cpp
void afterFork()
```


### function startThread

```cpp
void * startThread(
    void * obj
)
```


### function readDataBlock

```cpp
bool readDataBlock(
    File & f,
    struct TimeZone::Data * data,
    bool v1
)
```


### function readTimeZoneFile

```cpp
bool readTimeZoneFile(
    const char * zonefile,
    struct TimeZone::Data * data
)
```


### function fillHMS

```cpp
inline void fillHMS(
    unsigned seconds,
    struct DateTime * dt
)
```


### function BreakTime

```cpp
DateTime BreakTime(
    int64_t t
)
```



## Attributes Documentation

### variable require_32_bit_integer_at_least

```cpp
char[sizeof(int) >=sizeof(int32_t) ? 1 :-1] require_32_bit_integer_at_least;
```


### variable digits

```cpp
const char[] digits = "9876543210123456789";
```


### variable zero

```cpp
const char * zero = digits + 9;
```


### variable digitsHex

```cpp
const char[] digitsHex = "0123456789ABCDEF";
```


### variable kSmallBuffer

```cpp
const int kSmallBuffer = 4000;
```


### variable kLargeBuffer

```cpp
const int kLargeBuffer = 4000*1000;
```


### variable t_numOpenedFiles

```cpp
__thread int t_numOpenedFiles = 0;
```


### variable t_pids

```cpp
__thread std::vector< pid_t > * t_pids = NULL;
```


### variable g_startTime

```cpp
Timestamp g_startTime = Timestamp::now();
```


### variable g_clockTicks

```cpp
int g_clockTicks = static_cast<int>(::sysconf(_SC_CLK_TCK));
```


### variable g_pageSize

```cpp
int g_pageSize = static_cast<int>(::sysconf(_SC_PAGE_SIZE));
```


### variable init

```cpp
ThreadNameInitializer init;
```





-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800