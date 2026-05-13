---
title: SudokuStat

---

# SudokuStat






`#include <stat.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SudokuStat](/class_sudoku_stat.md#function-sudokustat)**(const ThreadPool & pool) |
| string | **[report](/class_sudoku_stat.md#function-report)**() const |
| string | **[reset](/class_sudoku_stat.md#function-reset)**() |
| void | **[recordResponse](/class_sudoku_stat.md#function-recordresponse)**([Timestamp](/class_timestamp.md) now, [Timestamp](/class_timestamp.md) receive, bool solved) |
| void | **[recordRequest](/class_sudoku_stat.md#function-recordrequest)**() |
| void | **[recordBadRequest](/class_sudoku_stat.md#function-recordbadrequest)**() |
| void | **[recordDroppedRequest](/class_sudoku_stat.md#function-recorddroppedrequest)**() |

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

### function SudokuStat

```cpp
inline SudokuStat(
    const ThreadPool & pool
)
```


### function report

```cpp
inline string report() const
```


### function reset

```cpp
inline string reset()
```


### function recordResponse

```cpp
inline void recordResponse(
    Timestamp now,
    Timestamp receive,
    bool solved
)
```


### function recordRequest

```cpp
inline void recordRequest()
```


### function recordBadRequest

```cpp
inline void recordBadRequest()
```


### function recordDroppedRequest

```cpp
inline void recordDroppedRequest()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800