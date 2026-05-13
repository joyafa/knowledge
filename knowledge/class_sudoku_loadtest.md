---
title: SudokuLoadtest

---

# SudokuLoadtest





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SudokuLoadtest](/class_sudoku_loadtest.md#function-sudokuloadtest)**() |
| void | **[runClient](/class_sudoku_loadtest.md#function-runclient)**(const [InputPtr](/sudoku_2loadtest_8cc.md#typedef-inputptr) & input, const [InetAddress](/class_inet_address.md) & serverAddr, int rps, int conn, bool nodelay) |

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

### function SudokuLoadtest

```cpp
inline SudokuLoadtest()
```


### function runClient

```cpp
inline void runClient(
    const InputPtr & input,
    const InetAddress & serverAddr,
    int rps,
    int conn,
    bool nodelay
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800