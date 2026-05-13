---
title: examples/maxconnection/main.cc

---

# examples/maxconnection/main.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/maxconnection_2main_8cc.md#function-main)**(int argc, char * argv[]) |


## Functions Documentation

### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```




## Source code

```cpp
#include "examples/maxconnection/echo.h"

#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"

#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

int main(int argc, char* argv[])
{
  LOG_INFO << "pid = " << getpid();
  EventLoop loop;
  InetAddress listenAddr(2007);
  int maxConnections = 5;
  if (argc > 1)
  {
    maxConnections = atoi(argv[1]);
  }
  LOG_INFO << "maxConnections = " << maxConnections;
  EchoServer server(&loop, listenAddr, maxConnections);
  server.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
