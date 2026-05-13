---
title: muduo::Logger

---

# muduo::Logger






`#include <Logging.h>`

## Public Classes

|                | Name           |
| -------------- | -------------- |
| class | **[SourceFile](/classmuduo_1_1_logger_1_1_source_file.md)**  |

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[LogLevel](/classmuduo_1_1_logger.md#enum-loglevel)** { TRACE, DEBUG, INFO, WARN, ERROR, FATAL, NUM_LOG_LEVELS} |
| typedef void(*)(const char *msg, int len) | **[OutputFunc](/classmuduo_1_1_logger.md#typedef-outputfunc)**  |
| typedef void(*)() | **[FlushFunc](/classmuduo_1_1_logger.md#typedef-flushfunc)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Logger](/classmuduo_1_1_logger.md#function-logger)**([SourceFile](/classmuduo_1_1_logger_1_1_source_file.md) file, int line) |
| | **[Logger](/classmuduo_1_1_logger.md#function-logger)**([SourceFile](/classmuduo_1_1_logger_1_1_source_file.md) file, int line, [LogLevel](/classmuduo_1_1_logger.md#enum-loglevel) level) |
| | **[Logger](/classmuduo_1_1_logger.md#function-logger)**([SourceFile](/classmuduo_1_1_logger_1_1_source_file.md) file, int line, [LogLevel](/classmuduo_1_1_logger.md#enum-loglevel) level, const char * func) |
| | **[Logger](/classmuduo_1_1_logger.md#function-logger)**([SourceFile](/classmuduo_1_1_logger_1_1_source_file.md) file, int line, bool toAbort) |
| | **[~Logger](/classmuduo_1_1_logger.md#function-~logger)**() |
| [LogStream](/classmuduo_1_1_log_stream.md) & | **[stream](/classmuduo_1_1_logger.md#function-stream)**() |
| [LogLevel](/classmuduo_1_1_logger.md#enum-loglevel) | **[logLevel](/classmuduo_1_1_logger.md#function-loglevel)**() |
| void | **[setLogLevel](/classmuduo_1_1_logger.md#function-setloglevel)**([LogLevel](/classmuduo_1_1_logger.md#enum-loglevel) level) |
| void | **[setOutput](/classmuduo_1_1_logger.md#function-setoutput)**([OutputFunc](/classmuduo_1_1_logger.md#typedef-outputfunc) out) |
| void | **[setFlush](/classmuduo_1_1_logger.md#function-setflush)**([FlushFunc](/classmuduo_1_1_logger.md#typedef-flushfunc) flush) |
| void | **[setTimeZone](/classmuduo_1_1_logger.md#function-settimezone)**(const [TimeZone](/class_time_zone.md) & tz) |

## Public Types Documentation

### enum LogLevel

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| TRACE | |   |
| DEBUG | |   |
| INFO | |   |
| WARN | |   |
| ERROR | |   |
| FATAL | |   |
| NUM_LOG_LEVELS | |   |




### typedef OutputFunc

```cpp
typedef void(* muduo::Logger::OutputFunc) (const char *msg, int len);
```


### typedef FlushFunc

```cpp
typedef void(* muduo::Logger::FlushFunc) ();
```


## Public Functions Documentation

### function Logger

```cpp
Logger(
    SourceFile file,
    int line
)
```


### function Logger

```cpp
Logger(
    SourceFile file,
    int line,
    LogLevel level
)
```


### function Logger

```cpp
Logger(
    SourceFile file,
    int line,
    LogLevel level,
    const char * func
)
```


### function Logger

```cpp
Logger(
    SourceFile file,
    int line,
    bool toAbort
)
```


### function ~Logger

```cpp
~Logger()
```


### function stream

```cpp
inline LogStream & stream()
```


### function logLevel

```cpp
static inline LogLevel logLevel()
```


### function setLogLevel

```cpp
static void setLogLevel(
    LogLevel level
)
```


### function setOutput

```cpp
static void setOutput(
    OutputFunc out
)
```


### function setFlush

```cpp
static void setFlush(
    FlushFunc flush
)
```


### function setTimeZone

```cpp
static void setTimeZone(
    const TimeZone & tz
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800