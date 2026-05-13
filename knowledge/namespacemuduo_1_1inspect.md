---
title: muduo::inspect

---

# muduo::inspect



## Functions

|                | Name           |
| -------------- | -------------- |
| string | **[uptime](/namespacemuduo_1_1inspect.md#function-uptime)**([Timestamp](/class_timestamp.md) now, [Timestamp](/class_timestamp.md) start, bool showMicroseconds) |
| long | **[getLong](/namespacemuduo_1_1inspect.md#function-getlong)**(const string & procStatus, const char * key) |
| string | **[getProcessName](/namespacemuduo_1_1inspect.md#function-getprocessname)**(const string & procStatus) |
| [StringPiece](/classmuduo_1_1_string_piece.md) | **[next](/namespacemuduo_1_1inspect.md#function-next)**([StringPiece](/classmuduo_1_1_string_piece.md) data) |
| [ProcessInfo::CpuTime](/structmuduo_1_1_process_info_1_1_cpu_time.md) | **[getCpuTime](/namespacemuduo_1_1inspect.md#function-getcputime)**([StringPiece](/classmuduo_1_1_string_piece.md) data) |
| int | **[stringPrintf](/namespacemuduo_1_1inspect.md#function-stringprintf)**(string * out, const char * fmt, ... ) |


## Functions Documentation

### function uptime

```cpp
string uptime(
    Timestamp now,
    Timestamp start,
    bool showMicroseconds
)
```


### function getLong

```cpp
long getLong(
    const string & procStatus,
    const char * key
)
```


### function getProcessName

```cpp
string getProcessName(
    const string & procStatus
)
```


### function next

```cpp
StringPiece next(
    StringPiece data
)
```


### function getCpuTime

```cpp
ProcessInfo::CpuTime getCpuTime(
    StringPiece data
)
```


### function stringPrintf

```cpp
int stringPrintf(
    string * out,
    const char * fmt,
    ... 
)
```






-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800