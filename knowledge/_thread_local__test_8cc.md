---
title: muduo/base/tests/ThreadLocal_test.cc

---

# muduo/base/tests/ThreadLocal_test.cc



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Test](/class_test.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[print](/_thread_local__test_8cc.md#function-print)**() |
| void | **[threadFunc](/_thread_local__test_8cc.md#function-threadfunc)**() |
| int | **[main](/_thread_local__test_8cc.md#function-main)**() |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [muduo::ThreadLocal](/classmuduo_1_1_thread_local.md)< [Test](/class_test.md) > | **[testObj1](/_thread_local__test_8cc.md#variable-testobj1)**  |
| [muduo::ThreadLocal](/classmuduo_1_1_thread_local.md)< [Test](/class_test.md) > | **[testObj2](/_thread_local__test_8cc.md#variable-testobj2)**  |


## Functions Documentation

### function print

```cpp
void print()
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

### variable testObj1

```cpp
muduo::ThreadLocal< Test > testObj1;
```


### variable testObj2

```cpp
muduo::ThreadLocal< Test > testObj2;
```



## Source code

```cpp
#include "muduo/base/ThreadLocal.h"
#include "muduo/base/CurrentThread.h"
#include "muduo/base/Thread.h"

#include <stdio.h>

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

muduo::ThreadLocal<Test> testObj1;
muduo::ThreadLocal<Test> testObj2;

void print()
{
  printf("tid=%d, obj1 %p name=%s\n",
         muduo::CurrentThread::tid(),
         &testObj1.value(),
         testObj1.value().name().c_str());
  printf("tid=%d, obj2 %p name=%s\n",
         muduo::CurrentThread::tid(),
         &testObj2.value(),
         testObj2.value().name().c_str());
}

void threadFunc()
{
  print();
  testObj1.value().setName("changed 1");
  testObj2.value().setName("changed 42");
  print();
}

int main()
{
  testObj1.value().setName("main one");
  print();
  muduo::Thread t1(threadFunc);
  t1.start();
  t1.join();
  testObj2.value().setName("main two");
  print();

  pthread_exit(0);
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
