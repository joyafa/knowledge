---
title: muduo/base/tests/FileUtil_test.cc

---

# muduo/base/tests/FileUtil_test.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/_file_util__test_8cc.md#function-main)**() |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[__STDC_FORMAT_MACROS](/_file_util__test_8cc.md#define---stdc-format-macros)**  |


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
#include "muduo/base/FileUtil.h"

#include <stdio.h>
#define __STDC_FORMAT_MACROS
#include <inttypes.h>

using namespace muduo;

int main()
{
  string result;
  int64_t size = 0;
  int err = FileUtil::readFile("/proc/self", 1024, &result, &size);
  printf("%d %zd %" PRIu64 "\n", err, result.size(), size);
  err = FileUtil::readFile("/proc/self", 1024, &result, NULL);
  printf("%d %zd %" PRIu64 "\n", err, result.size(), size);
  err = FileUtil::readFile("/proc/self/cmdline", 1024, &result, &size);
  printf("%d %zd %" PRIu64 "\n", err, result.size(), size);
  err = FileUtil::readFile("/dev/null", 1024, &result, &size);
  printf("%d %zd %" PRIu64 "\n", err, result.size(), size);
  err = FileUtil::readFile("/dev/zero", 1024, &result, &size);
  printf("%d %zd %" PRIu64 "\n", err, result.size(), size);
  err = FileUtil::readFile("/notexist", 1024, &result, &size);
  printf("%d %zd %" PRIu64 "\n", err, result.size(), size);
  err = FileUtil::readFile("/dev/zero", 102400, &result, &size);
  printf("%d %zd %" PRIu64 "\n", err, result.size(), size);
  err = FileUtil::readFile("/dev/zero", 102400, &result, NULL);
  printf("%d %zd %" PRIu64 "\n", err, result.size(), size);
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
