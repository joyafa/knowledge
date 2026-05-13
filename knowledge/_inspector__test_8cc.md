---
title: muduo/net/inspect/tests/Inspector_test.cc

---

# muduo/net/inspect/tests/Inspector_test.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/_inspector__test_8cc.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/net/inspect/Inspector.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/EventLoopThread.h"

using namespace muduo;
using namespace muduo::net;

int main()
{
  EventLoop loop;
  EventLoopThread t;
  Inspector ins(t.startLoop(), InetAddress(12345), "test");
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
