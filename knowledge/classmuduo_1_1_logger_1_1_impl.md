---
title: muduo::Logger::Impl

---

# muduo::Logger::Impl





## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [Logger::LogLevel](/classmuduo_1_1_logger.md#enum-loglevel) | **[LogLevel](/classmuduo_1_1_logger_1_1_impl.md#typedef-loglevel)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Impl](/classmuduo_1_1_logger_1_1_impl.md#function-impl)**([LogLevel](/classmuduo_1_1_logger.md#enum-loglevel) level, int old_errno, const [SourceFile](/classmuduo_1_1_logger_1_1_source_file.md) & file, int line) |
| void | **[formatTime](/classmuduo_1_1_logger_1_1_impl.md#function-formattime)**() |
| void | **[finish](/classmuduo_1_1_logger_1_1_impl.md#function-finish)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [Timestamp](/class_timestamp.md) | **[time_](/classmuduo_1_1_logger_1_1_impl.md#variable-time-)**  |
| [LogStream](/classmuduo_1_1_log_stream.md) | **[stream_](/classmuduo_1_1_logger_1_1_impl.md#variable-stream-)**  |
| [LogLevel](/classmuduo_1_1_logger.md#enum-loglevel) | **[level_](/classmuduo_1_1_logger_1_1_impl.md#variable-level-)**  |
| int | **[line_](/classmuduo_1_1_logger_1_1_impl.md#variable-line-)**  |
| [SourceFile](/classmuduo_1_1_logger_1_1_source_file.md) | **[basename_](/classmuduo_1_1_logger_1_1_impl.md#variable-basename-)**  |

## Public Types Documentation

### typedef LogLevel

```cpp
typedef Logger::LogLevel muduo::Logger::Impl::LogLevel;
```


## Public Functions Documentation

### function Impl

```cpp
Impl(
    LogLevel level,
    int old_errno,
    const SourceFile & file,
    int line
)
```


### function formatTime

```cpp
void formatTime()
```


### function finish

```cpp
void finish()
```


## Public Attributes Documentation

### variable time_

```cpp
Timestamp time_;
```


### variable stream_

```cpp
LogStream stream_;
```


### variable level_

```cpp
LogLevel level_;
```


### variable line_

```cpp
int line_;
```


### variable basename_

```cpp
SourceFile basename_;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800