---
title: muduo/net/tests/EventLoopThread_unittest.cc

---

# muduo/net/tests/EventLoopThread_unittest.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[print](/_event_loop_thread__unittest_8cc.md#function-print)**([EventLoop](/class_event_loop.md) * p =NULL) |
| void | **[quit](/_event_loop_thread__unittest_8cc.md#function-quit)**([EventLoop](/class_event_loop.md) * p) |
| int | **[main](/_event_loop_thread__unittest_8cc.md#function-main)**() |


## Functions Documentation

### function print

```cpp
void print(
    EventLoop * p =NULL
)
```


### function quit

```cpp
void quit(
    EventLoop * p
)
```


### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/net/EventLoopThread.h"
#include "muduo/net/EventLoop.h"
#include "muduo/base/Thread.h"
#include "muduo/base/CountDownLatch.h"

#include <stdio.h>
#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

void print(EventLoop* p = NULL)
{
  printf("print: pid = %d, tid = %d, loop = %p\n",
         getpid(), CurrentThread::tid(), p);
}

void quit(EventLoop* p)
{
  print(p);
  p->quit();
}

int main()
{
  print();

  {
  EventLoopThread thr1;  // never start
  }

  {
  // dtor calls quit()
  EventLoopThread thr2;
  EventLoop* loop = thr2.startLoop();
  loop->runInLoop(std::bind(print, loop));
  CurrentThread::sleepUsec(500 * 1000);
  }

  {
  // quit() before dtor
  EventLoopThread thr3;
  EventLoop* loop = thr3.startLoop();
  loop->runInLoop(std::bind(quit, loop));
  CurrentThread::sleepUsec(500 * 1000);
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
