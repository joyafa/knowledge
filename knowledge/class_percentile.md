---
title: Percentile

---

# Percentile






`#include <percentile.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Percentile](/class_percentile.md#function-percentile)**(std::vector< int > & latencies, int infly) |
| const [muduo::LogStream::Buffer](/classmuduo_1_1_log_stream.md#typedef-buffer) & | **[report](/class_percentile.md#function-report)**() const |
| void | **[save](/class_percentile.md#function-save)**(const std::vector< int > & latencies, [muduo::StringArg](/classmuduo_1_1_string_arg.md) name) const |

## Public Functions Documentation

### function Percentile

```cpp
inline Percentile(
    std::vector< int > & latencies,
    int infly
)
```


### function report

```cpp
inline const muduo::LogStream::Buffer & report() const
```


### function save

```cpp
inline void save(
    const std::vector< int > & latencies,
    muduo::StringArg name
) const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800