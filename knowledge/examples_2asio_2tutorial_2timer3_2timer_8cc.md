---
title: examples/asio/tutorial/timer3/timer.cc

---

# examples/asio/tutorial/timer3/timer.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[print](/examples_2asio_2tutorial_2timer3_2timer_8cc.md#function-print)**([muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * loop, int * count) |
| int | **[main](/examples_2asio_2tutorial_2timer3_2timer_8cc.md#function-main)**() |


## Functions Documentation

### function print

```cpp
void print(
    muduo::net::EventLoop * loop,
    int * count
)
```


### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/net/EventLoop.h"

#include <iostream>

void print(muduo::net::EventLoop* loop, int* count)
{
  if (*count < 5)
  {
    std::cout << *count << "\n";
    ++(*count);

    loop->runAfter(1, std::bind(print, loop, count));
  }
  else
  {
    loop->quit();
  }
}

int main()
{
  muduo::net::EventLoop loop;
  int count = 0;
  // Note: loop.runEvery() is better for this use case.
  loop.runAfter(1, std::bind(print, &loop, &count));
  loop.loop();
  std::cout << "Final count is " << count << "\n";
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
