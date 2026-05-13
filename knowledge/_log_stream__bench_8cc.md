---
title: muduo/base/tests/LogStream_bench.cc

---

# muduo/base/tests/LogStream_bench.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| template <typename T \> <br>void | **[benchPrintf](/_log_stream__bench_8cc.md#function-benchprintf)**(const char * fmt) |
| template <typename T \> <br>void | **[benchStringStream](/_log_stream__bench_8cc.md#function-benchstringstream)**() |
| template <typename T \> <br>void | **[benchLogStream](/_log_stream__bench_8cc.md#function-benchlogstream)**() |
| int | **[main](/_log_stream__bench_8cc.md#function-main)**() |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const size_t | **[N](/_log_stream__bench_8cc.md#variable-n)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[__STDC_FORMAT_MACROS](/_log_stream__bench_8cc.md#define---stdc-format-macros)**  |


## Functions Documentation

### function benchPrintf

```cpp
template <typename T >
void benchPrintf(
    const char * fmt
)
```


### function benchStringStream

```cpp
template <typename T >
void benchStringStream()
```


### function benchLogStream

```cpp
template <typename T >
void benchLogStream()
```


### function main

```cpp
int main()
```



## Attributes Documentation

### variable N

```cpp
const size_t N = 1000000;
```



## Macros Documentation

### define __STDC_FORMAT_MACROS

```cpp
#define __STDC_FORMAT_MACROS 
```


## Source code

```cpp
#include "muduo/base/LogStream.h"
#include "muduo/base/Timestamp.h"

#include <sstream>
#include <stdio.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>

using namespace muduo;

const size_t N = 1000000;

#pragma GCC diagnostic ignored "-Wold-style-cast"

template<typename T>
void benchPrintf(const char* fmt)
{
  char buf[32];
  Timestamp start(Timestamp::now());
  for (size_t i = 0; i < N; ++i)
    snprintf(buf, sizeof buf, fmt, (T)(i));
  Timestamp end(Timestamp::now());

  printf("benchPrintf %f\n", timeDifference(end, start));
}

template<typename T>
void benchStringStream()
{
  Timestamp start(Timestamp::now());
  std::ostringstream os;

  for (size_t i = 0; i < N; ++i)
  {
    os << (T)(i);
    os.seekp(0, std::ios_base::beg);
  }
  Timestamp end(Timestamp::now());

  printf("benchStringStream %f\n", timeDifference(end, start));
}

template<typename T>
void benchLogStream()
{
  Timestamp start(Timestamp::now());
  LogStream os;
  for (size_t i = 0; i < N; ++i)
  {
    os << (T)(i);
    os.resetBuffer();
  }
  Timestamp end(Timestamp::now());

  printf("benchLogStream %f\n", timeDifference(end, start));
}

int main()
{
  benchPrintf<int>("%d");

  puts("int");
  benchPrintf<int>("%d");
  benchStringStream<int>();
  benchLogStream<int>();

  puts("double");
  benchPrintf<double>("%.12g");
  benchStringStream<double>();
  benchLogStream<double>();

  puts("int64_t");
  benchPrintf<int64_t>("%" PRId64);
  benchStringStream<int64_t>();
  benchLogStream<int64_t>();

  puts("void*");
  benchPrintf<void*>("%p");
  benchStringStream<void*>();
  benchLogStream<void*>();

}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
