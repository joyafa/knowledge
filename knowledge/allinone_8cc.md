---
title: examples/simple/allinone/allinone.cc

---

# examples/simple/allinone/allinone.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/allinone_8cc.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
#include "examples/simple/chargen/chargen.h"
#include "examples/simple/daytime/daytime.h"
#include "examples/simple/discard/discard.h"
#include "examples/simple/echo/echo.h"
#include "examples/simple/time/time.h"

#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"

#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

int main()
{
  LOG_INFO << "pid = " << getpid();
  EventLoop loop;  // one loop shared by multiple servers

  ChargenServer chargenServer(&loop, InetAddress(2019));
  chargenServer.start();

  DaytimeServer daytimeServer(&loop, InetAddress(2013));
  daytimeServer.start();

  DiscardServer discardServer(&loop, InetAddress(2009));
  discardServer.start();

  EchoServer echoServer(&loop, InetAddress(2007));
  echoServer.start();

  TimeServer timeServer(&loop, InetAddress(2037));
  timeServer.start();

  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
