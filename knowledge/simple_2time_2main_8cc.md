---
title: examples/simple/time/main.cc

---

# examples/simple/time/main.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/simple_2time_2main_8cc.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
#include "examples/simple/time/time.h"

#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"

#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

int main()
{
  LOG_INFO << "pid = " << getpid();
  EventLoop loop;
  InetAddress listenAddr(2037);
  TimeServer server(&loop, listenAddr);
  server.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
