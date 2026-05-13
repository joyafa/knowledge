---
title: muduo/base/tests/Thread_test.cc

---

# muduo/base/tests/Thread_test.cc



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Foo](/class_foo.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[mysleep](/_thread__test_8cc.md#function-mysleep)**(int seconds) |
| void | **[threadFunc](/_thread__test_8cc.md#function-threadfunc)**() |
| void | **[threadFunc2](/_thread__test_8cc.md#function-threadfunc2)**(int x) |
| void | **[threadFunc3](/_thread__test_8cc.md#function-threadfunc3)**() |
| int | **[main](/_thread__test_8cc.md#function-main)**() |


## Functions Documentation

### function mysleep

```cpp
void mysleep(
    int seconds
)
```


### function threadFunc

```cpp
void threadFunc()
```


### function threadFunc2

```cpp
void threadFunc2(
    int x
)
```


### function threadFunc3

```cpp
void threadFunc3()
```


### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/base/Thread.h"
#include "muduo/base/CurrentThread.h"

#include <string>
#include <stdio.h>
#include <unistd.h>

void mysleep(int seconds)
{
  timespec t = { seconds, 0 };
  nanosleep(&t, NULL);
}

void threadFunc()
{
  printf("tid=%d\n", muduo::CurrentThread::tid());
}

void threadFunc2(int x)
{
  printf("tid=%d, x=%d\n", muduo::CurrentThread::tid(), x);
}

void threadFunc3()
{
  printf("tid=%d\n", muduo::CurrentThread::tid());
  mysleep(1);
}

class Foo
{
 public:
  explicit Foo(double x)
    : x_(x)
  {
  }

  void memberFunc()
  {
    printf("tid=%d, Foo::x_=%f\n", muduo::CurrentThread::tid(), x_);
  }

  void memberFunc2(const std::string& text)
  {
    printf("tid=%d, Foo::x_=%f, text=%s\n", muduo::CurrentThread::tid(), x_, text.c_str());
  }

 private:
  double x_;
};

int main()
{
  printf("pid=%d, tid=%d\n", ::getpid(), muduo::CurrentThread::tid());

  muduo::Thread t1(threadFunc);
  t1.start();
  printf("t1.tid=%d\n", t1.tid());
  t1.join();

  muduo::Thread t2(std::bind(threadFunc2, 42),
                   "thread for free function with argument");
  t2.start();
  printf("t2.tid=%d\n", t2.tid());
  t2.join();

  Foo foo(87.53);
  muduo::Thread t3(std::bind(&Foo::memberFunc, &foo),
                   "thread for member function without argument");
  t3.start();
  t3.join();

  muduo::Thread t4(std::bind(&Foo::memberFunc2, std::ref(foo), std::string("Shuo Chen")));
  t4.start();
  t4.join();

  {
    muduo::Thread t5(threadFunc3);
    t5.start();
    // t5 may destruct eariler than thread creation.
  }
  mysleep(2);
  {
    muduo::Thread t6(threadFunc3);
    t6.start();
    mysleep(2);
    // t6 destruct later than thread creation.
  }
  sleep(2);
  printf("number of created threads %d\n", muduo::Thread::numCreated());
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
