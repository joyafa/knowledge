---
title: muduo/net/tests/EventLoopThreadPool_unittest.cc

---

# muduo/net/tests/EventLoopThreadPool_unittest.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[print](/_event_loop_thread_pool__unittest_8cc.md#function-print)**([EventLoop](/class_event_loop.md) * p =NULL) |
| void | **[init](/_event_loop_thread_pool__unittest_8cc.md#function-init)**([EventLoop](/class_event_loop.md) * p) |
| int | **[main](/_event_loop_thread_pool__unittest_8cc.md#function-main)**() |


## Functions Documentation

### function print

```cpp
void print(
    EventLoop * p =NULL
)
```


### function init

```cpp
void init(
    EventLoop * p
)
```


### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/net/EventLoopThreadPool.h"
#include "muduo/net/EventLoop.h"
#include "muduo/base/Thread.h"

#include <stdio.h>
#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

void print(EventLoop* p = NULL)
{
  printf("main(): pid = %d, tid = %d, loop = %p\n",
         getpid(), CurrentThread::tid(), p);
}

void init(EventLoop* p)
{
  printf("init(): pid = %d, tid = %d, loop = %p\n",
         getpid(), CurrentThread::tid(), p);
}

int main()
{
  print();

  EventLoop loop;
  loop.runAfter(11, std::bind(&EventLoop::quit, &loop));

  {
    printf("Single thread %p:\n", &loop);
    EventLoopThreadPool model(&loop, "single");
    model.setThreadNum(0);
    model.start(init);
    assert(model.getNextLoop() == &loop);
    assert(model.getNextLoop() == &loop);
    assert(model.getNextLoop() == &loop);
  }

  {
    printf("Another thread:\n");
    EventLoopThreadPool model(&loop, "another");
    model.setThreadNum(1);
    model.start(init);
    EventLoop* nextLoop = model.getNextLoop();
    nextLoop->runAfter(2, std::bind(print, nextLoop));
    assert(nextLoop != &loop);
    assert(nextLoop == model.getNextLoop());
    assert(nextLoop == model.getNextLoop());
    ::sleep(3);
  }

  {
    printf("Three threads:\n");
    EventLoopThreadPool model(&loop, "three");
    model.setThreadNum(3);
    model.start(init);
    EventLoop* nextLoop = model.getNextLoop();
    nextLoop->runInLoop(std::bind(print, nextLoop));
    assert(nextLoop != &loop);
    assert(nextLoop != model.getNextLoop());
    assert(nextLoop != model.getNextLoop());
    assert(nextLoop == model.getNextLoop());
  }

  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
