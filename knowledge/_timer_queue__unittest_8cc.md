---
title: muduo/net/tests/TimerQueue_unittest.cc

---

# muduo/net/tests/TimerQueue_unittest.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[printTid](/_timer_queue__unittest_8cc.md#function-printtid)**() |
| void | **[print](/_timer_queue__unittest_8cc.md#function-print)**(const char * msg) |
| void | **[cancel](/_timer_queue__unittest_8cc.md#function-cancel)**([TimerId](/classmuduo_1_1net_1_1_timer_id.md) timer) |
| int | **[main](/_timer_queue__unittest_8cc.md#function-main)**() |

## Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[cnt](/_timer_queue__unittest_8cc.md#variable-cnt)**  |
| [EventLoop](/class_event_loop.md) * | **[g_loop](/_timer_queue__unittest_8cc.md#variable-g-loop)**  |


## Functions Documentation

### function printTid

```cpp
void printTid()
```


### function print

```cpp
void print(
    const char * msg
)
```


### function cancel

```cpp
void cancel(
    TimerId timer
)
```


### function main

```cpp
int main()
```



## Attributes Documentation

### variable cnt

```cpp
int cnt = 0;
```


### variable g_loop

```cpp
EventLoop * g_loop;
```



## Source code

```cpp
#include "muduo/net/EventLoop.h"
#include "muduo/net/EventLoopThread.h"
#include "muduo/base/Thread.h"

#include <stdio.h>
#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

int cnt = 0;
EventLoop* g_loop;

void printTid()
{
  printf("pid = %d, tid = %d\n", getpid(), CurrentThread::tid());
  printf("now %s\n", Timestamp::now().toString().c_str());
}

void print(const char* msg)
{
  printf("msg %s %s\n", Timestamp::now().toString().c_str(), msg);
  if (++cnt == 20)
  {
    g_loop->quit();
  }
}

void cancel(TimerId timer)
{
  g_loop->cancel(timer);
  printf("cancelled at %s\n", Timestamp::now().toString().c_str());
}

int main()
{
  printTid();
  sleep(1);
  {
    EventLoop loop;
    g_loop = &loop;

    print("main");
    loop.runAfter(1, std::bind(print, "once1"));
    loop.runAfter(1.5, std::bind(print, "once1.5"));
    loop.runAfter(2.5, std::bind(print, "once2.5"));
    loop.runAfter(3.5, std::bind(print, "once3.5"));
    TimerId t45 = loop.runAfter(4.5, std::bind(print, "once4.5"));
    loop.runAfter(4.2, std::bind(cancel, t45));
    loop.runAfter(4.8, std::bind(cancel, t45));
    loop.runEvery(2, std::bind(print, "every2"));
    TimerId t3 = loop.runEvery(3, std::bind(print, "every3"));
    loop.runAfter(9.001, std::bind(cancel, t3));

    loop.loop();
    print("main loop exits");
  }
  sleep(1);
  {
    EventLoopThread loopThread;
    EventLoop* loop = loopThread.startLoop();
    loop->runAfter(2, printTid);
    sleep(3);
    print("thread loop exits");
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
