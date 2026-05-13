---
title: muduo/base/tests/Mutex_test.cc

---

# muduo/base/tests/Mutex_test.cc



## Namespaces

| Name           |
| -------------- |
| **[std](/namespacestd.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[threadFunc](/_mutex__test_8cc.md#function-threadfunc)**() |
| int | **[foo](/_mutex__test_8cc.md#function-foo)**() |
| int | **[main](/_mutex__test_8cc.md#function-main)**() |

## Attributes

|                | Name           |
| -------------- | -------------- |
| MutexLock | **[g_mutex](/_mutex__test_8cc.md#variable-g-mutex)**  |
| vector< int > | **[g_vec](/_mutex__test_8cc.md#variable-g-vec)**  |
| const int | **[kCount](/_mutex__test_8cc.md#variable-kcount)**  |
| int | **[g_count](/_mutex__test_8cc.md#variable-g-count)**  |


## Functions Documentation

### function threadFunc

```cpp
void threadFunc()
```


### function foo

```cpp
int foo()
```


### function main

```cpp
int main()
```



## Attributes Documentation

### variable g_mutex

```cpp
MutexLock g_mutex;
```


### variable g_vec

```cpp
vector< int > g_vec;
```


### variable kCount

```cpp
const int kCount = 10*1000*1000;
```


### variable g_count

```cpp
int g_count = 0;
```



## Source code

```cpp
#include "muduo/base/CountDownLatch.h"
#include "muduo/base/Mutex.h"
#include "muduo/base/Thread.h"
#include "muduo/base/Timestamp.h"

#include <vector>
#include <stdio.h>

using namespace muduo;
using namespace std;

MutexLock g_mutex;
vector<int> g_vec;
const int kCount = 10*1000*1000;

void threadFunc()
{
  for (int i = 0; i < kCount; ++i)
  {
    MutexLockGuard lock(g_mutex);
    g_vec.push_back(i);
  }
}

int foo() __attribute__ ((noinline));

int g_count = 0;
int foo()
{
  MutexLockGuard lock(g_mutex);
  if (!g_mutex.isLockedByThisThread())
  {
    printf("FAIL\n");
    return -1;
  }

  ++g_count;
  return 0;
}

int main()
{
  printf("sizeof pthread_mutex_t: %zd\n", sizeof(pthread_mutex_t));
  printf("sizeof Mutex: %zd\n", sizeof(MutexLock));
  printf("sizeof pthread_cond_t: %zd\n", sizeof(pthread_cond_t));
  printf("sizeof Condition: %zd\n", sizeof(Condition));
  MCHECK(foo());
  if (g_count != 1)
  {
    printf("MCHECK calls twice.\n");
    abort();
  }

  const int kMaxThreads = 8;
  g_vec.reserve(kMaxThreads * kCount);

  Timestamp start(Timestamp::now());
  for (int i = 0; i < kCount; ++i)
  {
    g_vec.push_back(i);
  }

  printf("single thread without lock %f\n", timeDifference(Timestamp::now(), start));

  start = Timestamp::now();
  threadFunc();
  printf("single thread with lock %f\n", timeDifference(Timestamp::now(), start));

  for (int nthreads = 1; nthreads < kMaxThreads; ++nthreads)
  {
    std::vector<std::unique_ptr<Thread>> threads;
    g_vec.clear();
    start = Timestamp::now();
    for (int i = 0; i < nthreads; ++i)
    {
      threads.emplace_back(new Thread(&threadFunc));
      threads.back()->start();
    }
    for (int i = 0; i < nthreads; ++i)
    {
      threads[i]->join();
    }
    printf("%d thread(s) with lock %f\n", nthreads, timeDifference(Timestamp::now(), start));
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
