---
title: Plot

---

# Plot






`#include <plot.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[MyGdFont](/struct_plot_1_1_my_gd_font.md)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Plot](/class_plot.md#function-plot)**(int width, int height, int totalSeconds, int samplingPeriod) |
| | **[~Plot](/class_plot.md#function-~plot)**() |
| muduo::string | **[plotCpu](/class_plot.md#function-plotcpu)**(const std::vector< double > & data) |

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

### function Plot

```cpp
Plot(
    int width,
    int height,
    int totalSeconds,
    int samplingPeriod
)
```


### function ~Plot

```cpp
~Plot()
```


### function plotCpu

```cpp
muduo::string plotCpu(
    const std::vector< double > & data
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800