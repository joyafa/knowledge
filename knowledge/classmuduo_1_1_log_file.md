---
title: muduo::LogFile

---

# muduo::LogFile






`#include <LogFile.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[LogFile](/classmuduo_1_1_log_file.md#function-logfile)**(const string & basename, off_t rollSize, bool threadSafe =true, int flushInterval =3, int checkEveryN =1024) |
| | **[~LogFile](/classmuduo_1_1_log_file.md#function-~logfile)**() |
| void | **[append](/classmuduo_1_1_log_file.md#function-append)**(const char * logline, int len) |
| void | **[flush](/classmuduo_1_1_log_file.md#function-flush)**() |
| bool | **[rollFile](/classmuduo_1_1_log_file.md#function-rollfile)**() |

## Additional inherited members

**Public Functions inherited from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**(const noncopyable & ) =delete |
| void | **[operator=](/classmuduo_1_1noncopyable.md#function-operator=)**(const [noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable) & ) =delete |

**Protected Functions inherited from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**() =default |
| | **[~noncopyable](/classmuduo_1_1noncopyable.md#function-~noncopyable)**() =default |


## Public Functions Documentation

### function LogFile

```cpp
LogFile(
    const string & basename,
    off_t rollSize,
    bool threadSafe =true,
    int flushInterval =3,
    int checkEveryN =1024
)
```


### function ~LogFile

```cpp
~LogFile()
```


### function append

```cpp
void append(
    const char * logline,
    int len
)
```


### function flush

```cpp
void flush()
```


### function rollFile

```cpp
bool rollFile()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800