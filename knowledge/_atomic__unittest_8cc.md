---
title: muduo/base/tests/Atomic_unittest.cc

---

# muduo/base/tests/Atomic_unittest.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/_atomic__unittest_8cc.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/base/Atomic.h"
#include <assert.h>

int main()
{
  {
  muduo::AtomicInt64 a0;
  assert(a0.get() == 0);
  assert(a0.getAndAdd(1) == 0);
  assert(a0.get() == 1);
  assert(a0.addAndGet(2) == 3);
  assert(a0.get() == 3);
  assert(a0.incrementAndGet() == 4);
  assert(a0.get() == 4);
  a0.increment();
  assert(a0.get() == 5);
  assert(a0.addAndGet(-3) == 2);
  assert(a0.getAndSet(100) == 2);
  assert(a0.get() == 100);
  }

  {
  muduo::AtomicInt32 a1;
  assert(a1.get() == 0);
  assert(a1.getAndAdd(1) == 0);
  assert(a1.get() == 1);
  assert(a1.addAndGet(2) == 3);
  assert(a1.get() == 3);
  assert(a1.incrementAndGet() == 4);
  assert(a1.get() == 4);
  a1.increment();
  assert(a1.get() == 5);
  assert(a1.addAndGet(-3) == 2);
  assert(a1.getAndSet(100) == 2);
  assert(a1.get() == 100);
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
