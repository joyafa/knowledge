---
title: muduo/base/tests/ThreadPool_test.cc

---

# muduo/base/tests/ThreadPool_test.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[print](/_thread_pool__test_8cc.md#function-print)**() |
| void | **[printString](/_thread_pool__test_8cc.md#function-printstring)**(const std::string & str) |
| void | **[test](/_thread_pool__test_8cc.md#function-test)**(int maxSize) |
| void | **[longTask](/_thread_pool__test_8cc.md#function-longtask)**(int num) |
| void | **[test2](/_thread_pool__test_8cc.md#function-test2)**() |
| int | **[main](/_thread_pool__test_8cc.md#function-main)**() |


## Functions Documentation

### function print

```cpp
void print()
```


### function printString

```cpp
void printString(
    const std::string & str
)
```


### function test

```cpp
void test(
    int maxSize
)
```


### function longTask

```cpp
void longTask(
    int num
)
```


### function test2

```cpp
void test2()
```


### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/base/ThreadPool.h"
#include "muduo/base/CountDownLatch.h"
#include "muduo/base/CurrentThread.h"
#include "muduo/base/Logging.h"

#include <stdio.h>
#include <unistd.h>  // usleep

void print()
{
  printf("tid=%d\n", muduo::CurrentThread::tid());
}

void printString(const std::string& str)
{
  LOG_INFO << str;
  usleep(100*1000);
}

void test(int maxSize)
{
  LOG_WARN << "Test ThreadPool with max queue size = " << maxSize;
  muduo::ThreadPool pool("MainThreadPool");
  pool.setMaxQueueSize(maxSize);
  pool.start(5);

  LOG_WARN << "Adding";
  pool.run(print);
  pool.run(print);
  for (int i = 0; i < 100; ++i)
  {
    char buf[32];
    snprintf(buf, sizeof buf, "task %d", i);
    pool.run(std::bind(printString, std::string(buf)));
  }
  LOG_WARN << "Done";

  muduo::CountDownLatch latch(1);
  pool.run(std::bind(&muduo::CountDownLatch::countDown, &latch));
  latch.wait();
  pool.stop();
}

/*
 * Wish we could do this in the future.
void testMove()
{
  muduo::ThreadPool pool;
  pool.start(2);

  std::unique_ptr<int> x(new int(42));
  pool.run([y = std::move(x)]{ printf("%d: %d\n", muduo::CurrentThread::tid(), *y); });
  pool.stop();
}
*/

void longTask(int num)
{
  LOG_INFO << "longTask " << num;
  muduo::CurrentThread::sleepUsec(3000000);
}

void test2()
{
  LOG_WARN << "Test ThreadPool by stoping early.";
  muduo::ThreadPool pool("ThreadPool");
  pool.setMaxQueueSize(5);
  pool.start(3);

  muduo::Thread thread1([&pool]()
  {
    for (int i = 0; i < 20; ++i)
    {
      pool.run(std::bind(longTask, i));
    }
  }, "thread1");
  thread1.start();

  muduo::CurrentThread::sleepUsec(5000000);
  LOG_WARN << "stop pool";
  pool.stop();  // early stop

  thread1.join();
  // run() after stop()
  pool.run(print);
  LOG_WARN << "test2 Done";
}

int main()
{
  test(0);
  test(1);
  test(5);
  test(10);
  test(50);
  test2();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
