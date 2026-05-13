---
title: muduo/net/tests/EventLoop_unittest.cc

---

# muduo/net/tests/EventLoop_unittest.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[callback](/_event_loop__unittest_8cc.md#function-callback)**() |
| void | **[threadFunc](/_event_loop__unittest_8cc.md#function-threadfunc)**() |
| int | **[main](/_event_loop__unittest_8cc.md#function-main)**() |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [EventLoop](/class_event_loop.md) * | **[g_loop](/_event_loop__unittest_8cc.md#variable-g-loop)**  |


## Functions Documentation

### function callback

```cpp
void callback()
```


### function threadFunc

```cpp
void threadFunc()
```


### function main

```cpp
int main()
```



## Attributes Documentation

### variable g_loop

```cpp
EventLoop * g_loop;
```



## Source code

```cpp
#include "muduo/net/EventLoop.h"
#include "muduo/base/Thread.h"

#include <assert.h>
#include <stdio.h>
#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

EventLoop* g_loop;

void callback()
{
  printf("callback(): pid = %d, tid = %d\n", getpid(), CurrentThread::tid());
  EventLoop anotherLoop;
}

void threadFunc()
{
  printf("threadFunc(): pid = %d, tid = %d\n", getpid(), CurrentThread::tid());

  assert(EventLoop::getEventLoopOfCurrentThread() == NULL);
  EventLoop loop;
  assert(EventLoop::getEventLoopOfCurrentThread() == &loop);
  loop.runAfter(1.0, callback);
  loop.loop();
}

int main()
{
  printf("main(): pid = %d, tid = %d\n", getpid(), CurrentThread::tid());

  assert(EventLoop::getEventLoopOfCurrentThread() == NULL);
  EventLoop loop;
  assert(EventLoop::getEventLoopOfCurrentThread() == &loop);

  Thread thread(threadFunc);
  thread.start();

  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
