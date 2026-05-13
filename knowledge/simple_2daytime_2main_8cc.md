---
title: examples/simple/daytime/main.cc

---

# examples/simple/daytime/main.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/simple_2daytime_2main_8cc.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
#include "examples/simple/daytime/daytime.h"

#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"

#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

int main()
{
  LOG_INFO << "pid = " << getpid();
  EventLoop loop;
  InetAddress listenAddr(2013);
  DaytimeServer server(&loop, listenAddr);
  server.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
