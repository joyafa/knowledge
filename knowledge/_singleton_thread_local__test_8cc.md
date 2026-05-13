---
title: muduo/base/tests/SingletonThreadLocal_test.cc

---

# muduo/base/tests/SingletonThreadLocal_test.cc



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Test](/class_test.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[print](/_singleton_thread_local__test_8cc.md#function-print)**() |
| void | **[threadFunc](/_singleton_thread_local__test_8cc.md#function-threadfunc)**(const char * changeTo) |
| int | **[main](/_singleton_thread_local__test_8cc.md#function-main)**() |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[STL](/_singleton_thread_local__test_8cc.md#define-stl)**  |


## Functions Documentation

### function print

```cpp
void print()
```


### function threadFunc

```cpp
void threadFunc(
    const char * changeTo
)
```


### function main

```cpp
int main()
```




## Macros Documentation

### define STL

```cpp
#define STL muduo::Singleton<muduo::ThreadLocal<Test> >::instance().value()
```


## Source code

```cpp
#include "muduo/base/Singleton.h"
#include "muduo/base/CurrentThread.h"
#include "muduo/base/ThreadLocal.h"
#include "muduo/base/Thread.h"

#include <stdio.h>
#include <unistd.h>

class Test : muduo::noncopyable
{
 public:
  Test()
  {
    printf("tid=%d, constructing %p\n", muduo::CurrentThread::tid(), this);
  }

  ~Test()
  {
    printf("tid=%d, destructing %p %s\n", muduo::CurrentThread::tid(), this, name_.c_str());
  }

  const muduo::string& name() const { return name_; }
  void setName(const muduo::string& n) { name_ = n; }

 private:
  muduo::string name_;
};

#define STL muduo::Singleton<muduo::ThreadLocal<Test> >::instance().value()

void print()
{
  printf("tid=%d, %p name=%s\n",
         muduo::CurrentThread::tid(),
         &STL,
         STL.name().c_str());
}

void threadFunc(const char* changeTo)
{
  print();
  STL.setName(changeTo);
  sleep(1);
  print();
}

int main()
{
  STL.setName("main one");
  muduo::Thread t1(std::bind(threadFunc, "thread1"));
  muduo::Thread t2(std::bind(threadFunc, "thread2"));
  t1.start();
  t2.start();
  t1.join();
  print();
  t2.join();
  pthread_exit(0);
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
