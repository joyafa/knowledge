---
title: muduo::AsyncLogging

---

# muduo::AsyncLogging






`#include <AsyncLogging.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[AsyncLogging](/classmuduo_1_1_async_logging.md#function-asynclogging)**(const string & basename, off_t rollSize, int flushInterval =3) |
| | **[~AsyncLogging](/classmuduo_1_1_async_logging.md#function-~asynclogging)**() |
| void | **[append](/classmuduo_1_1_async_logging.md#function-append)**(const char * logline, int len) |
| void | **[start](/classmuduo_1_1_async_logging.md#function-start)**() |
| void | **[stop](/classmuduo_1_1_async_logging.md#function-stop)**() |

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

### function AsyncLogging

```cpp
AsyncLogging(
    const string & basename,
    off_t rollSize,
    int flushInterval =3
)
```


### function ~AsyncLogging

```cpp
inline ~AsyncLogging()
```


### function append

```cpp
void append(
    const char * logline,
    int len
)
```


### function start

```cpp
inline void start()
```


### function stop

```cpp
inline void stop()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800