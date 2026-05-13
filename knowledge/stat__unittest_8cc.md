---
title: examples/sudoku/stat_unittest.cc

---

# examples/sudoku/stat_unittest.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| | **[BOOST_AUTO_TEST_CASE](/stat__unittest_8cc.md#function-boost-auto-test-case)**(testSudokuStatSameSecond ) |
| | **[BOOST_AUTO_TEST_CASE](/stat__unittest_8cc.md#function-boost-auto-test-case)**(testSudokuStatNextSecond ) |
| | **[BOOST_AUTO_TEST_CASE](/stat__unittest_8cc.md#function-boost-auto-test-case)**(testSudokuStatFuzz ) |
| | **[BOOST_AUTO_TEST_CASE](/stat__unittest_8cc.md#function-boost-auto-test-case)**(testSudokuStatJumpAhead5 ) |
| | **[BOOST_AUTO_TEST_CASE](/stat__unittest_8cc.md#function-boost-auto-test-case)**(testSudokuStatJumpAhead59 ) |
| | **[BOOST_AUTO_TEST_CASE](/stat__unittest_8cc.md#function-boost-auto-test-case)**(testSudokuStatJumpAhead60 ) |
| | **[BOOST_AUTO_TEST_CASE](/stat__unittest_8cc.md#function-boost-auto-test-case)**(testSudokuStatJumpBack3 ) |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BOOST_TEST_MAIN](/stat__unittest_8cc.md#define-boost-test-main)**  |
|  | **[BOOST_TEST_DYN_LINK](/stat__unittest_8cc.md#define-boost-test-dyn-link)**  |


## Functions Documentation

### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testSudokuStatSameSecond 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testSudokuStatNextSecond 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testSudokuStatFuzz 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testSudokuStatJumpAhead5 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testSudokuStatJumpAhead59 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testSudokuStatJumpAhead60 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testSudokuStatJumpBack3 
)
```




## Macros Documentation

### define BOOST_TEST_MAIN

```cpp
#define BOOST_TEST_MAIN 
```


### define BOOST_TEST_DYN_LINK

```cpp
#define BOOST_TEST_DYN_LINK 
```


## Source code

```cpp
#include "muduo/base/Logging.h"
#include "muduo/base/Thread.h"
#include "muduo/base/ThreadPool.h"

#include <boost/circular_buffer.hpp>
#define BOOST_TEST_MAIN
#define BOOST_TEST_DYN_LINK
#include <boost/test/unit_test.hpp>

using namespace muduo;

#include "examples/sudoku/stat.h"

#include <stdio.h>

BOOST_AUTO_TEST_CASE(testSudokuStatSameSecond)
{
  ThreadPool p;
  SudokuStat s(p);

  for (int i = 0; i < 100; ++i)
  {
    time_t start = 1234567890;
    Timestamp recv = Timestamp::fromUnixTime(start, 0);
    Timestamp send = Timestamp::fromUnixTime(start, i);
    s.recordResponse(send, recv, i % 3 != 0);
  }
  printf("same second:\n%s\n", s.report().c_str());
}

BOOST_AUTO_TEST_CASE(testSudokuStatNextSecond)
{
  ThreadPool p;
  SudokuStat s(p);

  time_t start = 1234567890;
  Timestamp recv = Timestamp::fromUnixTime(start, 0);
  Timestamp send = addTime(recv, 0.002);
  for (int i = 0; i < 10000; ++i)
  {
    s.recordResponse(send, recv, true);
    recv = addTime(send, 0.01);
    send = addTime(recv, 0.02);
  }
  printf("next second:\n%s\n", s.report().c_str());
}

BOOST_AUTO_TEST_CASE(testSudokuStatFuzz)
{
  ThreadPool p;
  SudokuStat s(p);

  time_t start = 1234567890;
  srand(static_cast<unsigned>(time(NULL)));
  for (int i = 0; i < 10000; ++i)
  {
    Timestamp recv = Timestamp::fromUnixTime(start, 0);
    Timestamp send = Timestamp::fromUnixTime(start, 200);
    s.recordResponse(send, recv, true);
    int jump = (rand() % 200) - 100;
    // printf("%4d ", jump);
    start += jump;
  }
}

BOOST_AUTO_TEST_CASE(testSudokuStatJumpAhead5)
{
  ThreadPool p;
  SudokuStat s(p);

  time_t start = 1234567890;
  Timestamp recv = Timestamp::fromUnixTime(start, 0);
  Timestamp send = Timestamp::fromUnixTime(start, 200);
  s.recordResponse(send, recv, true);

  recv = addTime(recv, 4);
  send = addTime(send, 5);
  s.recordResponse(send, recv, true);
  printf("jump ahead 5 seconds:\n%s\n", s.report().c_str());
}

BOOST_AUTO_TEST_CASE(testSudokuStatJumpAhead59)
{
  ThreadPool p;
  SudokuStat s(p);

  time_t start = 1234567890;
  Timestamp recv = Timestamp::fromUnixTime(start, 0);
  Timestamp send = Timestamp::fromUnixTime(start, 200);
  s.recordResponse(send, recv, true);

  recv = addTime(recv, 55);
  send = addTime(send, 59);
  s.recordResponse(send, recv, true);
  printf("jump ahead 59 seconds:\n%s\n", s.report().c_str());
}

BOOST_AUTO_TEST_CASE(testSudokuStatJumpAhead60)
{
  ThreadPool p;
  SudokuStat s(p);

  time_t start = 1234567890;
  Timestamp recv = Timestamp::fromUnixTime(start, 0);
  Timestamp send = Timestamp::fromUnixTime(start, 200);
  s.recordResponse(send, recv, true);

  recv = addTime(recv, 58);
  send = addTime(send, 60);
  s.recordResponse(send, recv, true);
  printf("jump ahead 60 seconds:\n%s\n", s.report().c_str());
}

BOOST_AUTO_TEST_CASE(testSudokuStatJumpBack3)
{
  ThreadPool p;
  SudokuStat s(p);

  time_t start = 1234567890;
  Timestamp recv = Timestamp::fromUnixTime(start, 0);
  Timestamp send = Timestamp::fromUnixTime(start, 200);
  s.recordResponse(send, recv, true);

  recv = addTime(recv, 9);
  send = addTime(send, 10);
  s.recordResponse(send, recv, true);

  recv = addTime(recv, -4);
  send = addTime(send, -3);
  s.recordResponse(send, recv, true);

  printf("jump back 3 seconds:\n%s\n", s.report().c_str());
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
