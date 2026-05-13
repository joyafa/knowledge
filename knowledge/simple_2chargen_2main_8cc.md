---
title: examples/simple/chargen/main.cc

---

# examples/simple/chargen/main.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/simple_2chargen_2main_8cc.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
#include "examples/simple/chargen/chargen.h"

#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"

#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

int main()
{
  LOG_INFO << "pid = " << getpid();
  EventLoop loop;
  InetAddress listenAddr(2019);
  ChargenServer server(&loop, listenAddr, true);
  server.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
