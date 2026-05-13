---
title: examples/asio/tutorial/timer2/timer.cc

---

# examples/asio/tutorial/timer2/timer.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[print](/examples_2asio_2tutorial_2timer2_2timer_8cc.md#function-print)**() |
| int | **[main](/examples_2asio_2tutorial_2timer2_2timer_8cc.md#function-main)**() |


## Functions Documentation

### function print

```cpp
void print()
```


### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/net/EventLoop.h"

#include <iostream>

void print()
{
  std::cout << "Hello, world!\n";
}

int main()
{
  muduo::net::EventLoop loop;
  loop.runAfter(5, print);
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
