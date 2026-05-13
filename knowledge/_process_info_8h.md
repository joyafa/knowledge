---
title: muduo/base/ProcessInfo.h

---

# muduo/base/ProcessInfo.h



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |
| **[muduo::ProcessInfo](/namespacemuduo_1_1_process_info.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[muduo::ProcessInfo::CpuTime](/structmuduo_1_1_process_info_1_1_cpu_time.md)**  |




## Source code

```cpp
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.

// Author: Shuo Chen (chenshuo at chenshuo dot com)
//
// This is a public header file, it must only include public header files.

#ifndef MUDUO_BASE_PROCESSINFO_H
#define MUDUO_BASE_PROCESSINFO_H

#include "muduo/base/StringPiece.h"
#include "muduo/base/Types.h"
#include "muduo/base/Timestamp.h"
#include <vector>
#include <sys/types.h>

namespace muduo
{

namespace ProcessInfo
{
  pid_t pid();
  string pidString();
  uid_t uid();
  string username();
  uid_t euid();
  Timestamp startTime();
  int clockTicksPerSecond();
  int pageSize();
  bool isDebugBuild();  // constexpr

  string hostname();
  string procname();
  StringPiece procname(const string& stat);

  string procStatus();

  string procStat();

  string threadStat();

  string exePath();

  int openedFiles();
  int maxOpenFiles();

  struct CpuTime
  {
    double userSeconds;
    double systemSeconds;

    CpuTime() : userSeconds(0.0), systemSeconds(0.0) { }

    double total() const { return userSeconds + systemSeconds; }
  };
  CpuTime cpuTime();

  int numThreads();
  std::vector<pid_t> threads();
}  // namespace ProcessInfo

}  // namespace muduo

#endif  // MUDUO_BASE_PROCESSINFO_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
