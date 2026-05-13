---
title: muduo/base/tests/Timestamp_unittest.cc

---

# muduo/base/tests/Timestamp_unittest.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[passByConstReference](/_timestamp__unittest_8cc.md#function-passbyconstreference)**(const [Timestamp](/class_timestamp.md) & x) |
| void | **[passByValue](/_timestamp__unittest_8cc.md#function-passbyvalue)**([Timestamp](/class_timestamp.md) x) |
| void | **[benchmark](/_timestamp__unittest_8cc.md#function-benchmark)**() |
| int | **[main](/_timestamp__unittest_8cc.md#function-main)**() |


## Functions Documentation

### function passByConstReference

```cpp
void passByConstReference(
    const Timestamp & x
)
```


### function passByValue

```cpp
void passByValue(
    Timestamp x
)
```


### function benchmark

```cpp
void benchmark()
```


### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/base/Timestamp.h"
#include <vector>
#include <stdio.h>

using muduo::Timestamp;

void passByConstReference(const Timestamp& x)
{
  printf("%s\n", x.toString().c_str());
}

void passByValue(Timestamp x)
{
  printf("%s\n", x.toString().c_str());
}

void benchmark()
{
  const int kNumber = 1000*1000;

  std::vector<Timestamp> stamps;
  stamps.reserve(kNumber);
  for (int i = 0; i < kNumber; ++i)
  {
    stamps.push_back(Timestamp::now());
  }
  printf("%s\n", stamps.front().toString().c_str());
  printf("%s\n", stamps.back().toString().c_str());
  printf("%f\n", timeDifference(stamps.back(), stamps.front()));

  int increments[100] = { 0 };
  int64_t start = stamps.front().microSecondsSinceEpoch();
  for (int i = 1; i < kNumber; ++i)
  {
    int64_t next = stamps[i].microSecondsSinceEpoch();
    int64_t inc = next - start;
    start = next;
    if (inc < 0)
    {
      printf("reverse!\n");
    }
    else if (inc < 100)
    {
      ++increments[inc];
    }
    else
    {
      printf("big gap %d\n", static_cast<int>(inc));
    }
  }

  for (int i = 0; i < 100; ++i)
  {
    printf("%2d: %d\n", i, increments[i]);
  }
}

int main()
{
  Timestamp now(Timestamp::now());
  printf("%s\n", now.toString().c_str());
  passByValue(now);
  passByConstReference(now);
  benchmark();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
