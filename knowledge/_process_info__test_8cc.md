---
title: muduo/base/tests/ProcessInfo_test.cc

---

# muduo/base/tests/ProcessInfo_test.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/_process_info__test_8cc.md#function-main)**() |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[__STDC_FORMAT_MACROS](/_process_info__test_8cc.md#define---stdc-format-macros)**  |


## Functions Documentation

### function main

```cpp
int main()
```




## Macros Documentation

### define __STDC_FORMAT_MACROS

```cpp
#define __STDC_FORMAT_MACROS 
```


## Source code

```cpp
#include "muduo/base/ProcessInfo.h"
#include <stdio.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>

int main()
{
  printf("pid = %d\n", muduo::ProcessInfo::pid());
  printf("uid = %d\n", muduo::ProcessInfo::uid());
  printf("euid = %d\n", muduo::ProcessInfo::euid());
  printf("start time = %s\n", muduo::ProcessInfo::startTime().toFormattedString().c_str());
  printf("hostname = %s\n", muduo::ProcessInfo::hostname().c_str());
  printf("opened files = %d\n", muduo::ProcessInfo::openedFiles());
  printf("threads = %zd\n", muduo::ProcessInfo::threads().size());
  printf("num threads = %d\n", muduo::ProcessInfo::numThreads());
  printf("status = %s\n", muduo::ProcessInfo::procStatus().c_str());
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
