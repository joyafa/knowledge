---
title: examples/twisted/finger/finger02.cc

---

# examples/twisted/finger/finger02.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/finger02_8cc.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/net/EventLoop.h"
#include "muduo/net/TcpServer.h"

using namespace muduo;
using namespace muduo::net;

int main()
{
  EventLoop loop;
  TcpServer server(&loop, InetAddress(1079), "Finger");
  server.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
