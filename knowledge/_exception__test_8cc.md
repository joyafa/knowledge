---
title: muduo/base/tests/Exception_test.cc

---

# muduo/base/tests/Exception_test.cc



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Bar](/class_bar.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[foo](/_exception__test_8cc.md#function-foo)**() |
| int | **[main](/_exception__test_8cc.md#function-main)**() |


## Functions Documentation

### function foo

```cpp
void foo()
```


### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/base/CurrentThread.h"
#include "muduo/base/Exception.h"
#include <functional>
#include <vector>
#include <stdio.h>

class Bar
{
 public:
  void test(std::vector<std::string> names = {})
  {
    printf("Stack:\n%s\n", muduo::CurrentThread::stackTrace(true).c_str());
    [] {
      printf("Stack inside lambda:\n%s\n", muduo::CurrentThread::stackTrace(true).c_str());
    }();
    std::function<void()> func([] {
      printf("Stack inside std::function:\n%s\n", muduo::CurrentThread::stackTrace(true).c_str());
    });
    func();

    func = std::bind(&Bar::callback, this);
    func();

    throw muduo::Exception("oops");
  }

 private:
   void callback()
   {
     printf("Stack inside std::bind:\n%s\n", muduo::CurrentThread::stackTrace(true).c_str());
   }
};

void foo()
{
  Bar b;
  b.test();
}

int main()
{
  try
  {
    foo();
  }
  catch (const muduo::Exception& ex)
  {
    printf("reason: %s\n", ex.what());
    printf("stack trace:\n%s\n", ex.stackTrace());
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
