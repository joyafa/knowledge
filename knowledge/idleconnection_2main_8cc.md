---
title: examples/idleconnection/main.cc

---

# examples/idleconnection/main.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/idleconnection_2main_8cc.md#function-main)**(int argc, char * argv[]) |


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
#include "examples/idleconnection/echo.h"
#include <stdio.h>

#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"

using namespace muduo;
using namespace muduo::net;

/*
void testHash()
{
  boost::hash<std::shared_ptr<int> > h;
  std::shared_ptr<int> x1(new int(10));
  std::shared_ptr<int> x2(new int(10));
  h(x1);
  assert(h(x1) != h(x2));
  x1 = x2;
  assert(h(x1) == h(x2));
  x1.reset();
  assert(h(x1) != h(x2));
  x2.reset();
  assert(h(x1) == h(x2));
}
*/

int main(int argc, char* argv[])
{
  // testHash();
  EventLoop loop;
  InetAddress listenAddr(2007);
  int idleSeconds = 10;
  if (argc > 1)
  {
    idleSeconds = atoi(argv[1]);
  }
  LOG_INFO << "pid = " << getpid() << ", idle seconds = " << idleSeconds;
  EchoServer server(&loop, listenAddr, idleSeconds);
  server.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
