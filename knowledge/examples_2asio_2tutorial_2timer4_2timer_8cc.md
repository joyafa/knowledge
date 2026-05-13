---
title: examples/asio/tutorial/timer4/timer.cc

---

# examples/asio/tutorial/timer4/timer.cc



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Printer](/class_printer.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/examples_2asio_2tutorial_2timer4_2timer_8cc.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/net/EventLoop.h"

#include <iostream>

class Printer : muduo::noncopyable
{
 public:
  Printer(muduo::net::EventLoop* loop)
    : loop_(loop),
      count_(0)
  {
    // Note: loop.runEvery() is better for this use case.
    loop_->runAfter(1, std::bind(&Printer::print, this));
  }

  ~Printer()
  {
    std::cout << "Final count is " << count_ << "\n";
  }

  void print()
  {
    if (count_ < 5)
    {
      std::cout << count_ << "\n";
      ++count_;

      loop_->runAfter(1, std::bind(&Printer::print, this));
    }
    else
    {
      loop_->quit();
    }
  }

private:
  muduo::net::EventLoop* loop_;
  int count_;
};

int main()
{
  muduo::net::EventLoop loop;
  Printer printer(&loop);
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
