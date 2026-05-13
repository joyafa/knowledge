---
title: examples/sudoku/sudoku.h

---

# examples/sudoku/sudoku.h



## Functions

|                | Name           |
| -------------- | -------------- |
| muduo::string | **[solveSudoku](/sudoku_8h.md#function-solvesudoku)**(const [muduo::StringPiece](/classmuduo_1_1_string_piece.md) & puzzle) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const int | **[kCells](/sudoku_8h.md#variable-kcells)**  |
| const char[] | **[kNoSolution](/sudoku_8h.md#variable-knosolution)**  |


## Functions Documentation

### function solveSudoku

```cpp
muduo::string solveSudoku(
    const muduo::StringPiece & puzzle
)
```



## Attributes Documentation

### variable kCells

```cpp
const int kCells = 81;
```


### variable kNoSolution

```cpp
const char[] kNoSolution;
```



## Source code

```cpp
#ifndef MUDUO_EXAMPLES_SUDOKU_SUDOKU_H
#define MUDUO_EXAMPLES_SUDOKU_SUDOKU_H


#include "muduo/base/Types.h"
#include "muduo/base/StringPiece.h"

muduo::string solveSudoku(const muduo::StringPiece& puzzle);
const int kCells = 81;
extern const char kNoSolution[];

#endif  // MUDUO_EXAMPLES_SUDOKU_SUDOKU_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
