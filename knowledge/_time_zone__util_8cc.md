---
title: muduo/base/tests/TimeZone_util.cc

---

# muduo/base/tests/TimeZone_util.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[printUtcAndLocal](/_time_zone__util_8cc.md#function-printutcandlocal)**(int64_t utc, [TimeZone](/class_time_zone.md) local) |
| int | **[main](/_time_zone__util_8cc.md#function-main)**(int argc, char * argv[]) |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[__STDC_FORMAT_MACROS](/_time_zone__util_8cc.md#define---stdc-format-macros)**  |


## Functions Documentation

### function printUtcAndLocal

```cpp
void printUtcAndLocal(
    int64_t utc,
    TimeZone local
)
```


### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```




## Macros Documentation

### define __STDC_FORMAT_MACROS

```cpp
#define __STDC_FORMAT_MACROS 
```


## Source code

```cpp
#include "muduo/base/TimeZone.h"

#include <assert.h>

#ifndef __STDC_FORMAT_MACROS
#define __STDC_FORMAT_MACROS
#endif

#include <inttypes.h>

#include <string>

using muduo::DateTime;
using muduo::TimeZone;

void printUtcAndLocal(int64_t utc, TimeZone local)
{
  printf("Unix Time: %" PRId64 "\n", utc);
  printf("UTC:       %s\n", TimeZone::toUtcTime(utc).toIsoString().c_str());
  int utcOffset = 0;
  printf("Local:     %s", local.toLocalTime(utc, &utcOffset).toIsoString().c_str());
  printf(" %+03d%02d\n", utcOffset / 3600, utcOffset % 3600 / 60);
}

int main(int argc, char* argv[])
{
  TimeZone local = TimeZone::loadZoneFile("/etc/localtime");
  if (argc <= 1)
  {
    time_t now = ::time(NULL);
    printUtcAndLocal(now, local);
    return 0;
  }

  // TODO: input is from a different timezone.

  for (int i = 1; i < argc; ++i)
  {
    char* end = NULL;
    int64_t t = strtol(argv[i], &end, 10);
    if (end > argv[i] && *end == '\0')
    {
      printUtcAndLocal(t, local);
    }
    else
    {
      struct tm tm = { };
      end = strptime(argv[i], "%F %T", &tm);
      if (end != NULL && *end == '\0')
      {
        DateTime dt(tm);
        t = local.fromLocalTime(dt);
        printUtcAndLocal(t, local);
      }
    }
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
