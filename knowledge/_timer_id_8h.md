---
title: muduo/net/TimerId.h

---

# muduo/net/TimerId.h



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |
| **[muduo::net](/namespacemuduo_1_1net.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::net::TimerId](/classmuduo_1_1net_1_1_timer_id.md)**  |




## Source code

```cpp
// Copyright 2010, Shuo Chen.  All rights reserved.
// http://code.google.com/p/muduo/
//
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.

// Author: Shuo Chen (chenshuo at chenshuo dot com)
//
// This is a public header file, it must only include public header files.

#ifndef MUDUO_NET_TIMERID_H
#define MUDUO_NET_TIMERID_H

#include "muduo/base/copyable.h"

namespace muduo
{
namespace net
{

class Timer;

class TimerId : public muduo::copyable
{
 public:
  TimerId()
    : timer_(NULL),
      sequence_(0)
  {
  }

  TimerId(Timer* timer, int64_t seq)
    : timer_(timer),
      sequence_(seq)
  {
  }

  // default copy-ctor, dtor and assignment are okay

  friend class TimerQueue;

 private:
  Timer* timer_;
  int64_t sequence_;
};

}  // namespace net
}  // namespace muduo

#endif  // MUDUO_NET_TIMERID_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
