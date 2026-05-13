---
title: muduo/base/Exception.h

---

# muduo/base/Exception.h



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::Exception](/classmuduo_1_1_exception.md)**  |




## Source code

```cpp
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.
//
// Author: Shuo Chen (chenshuo at chenshuo dot com)

#ifndef MUDUO_BASE_EXCEPTION_H
#define MUDUO_BASE_EXCEPTION_H

#include "muduo/base/Types.h"
#include <exception>

namespace muduo
{

class Exception : public std::exception
{
 public:
  Exception(string what);
  ~Exception() noexcept override = default;

  // default copy-ctor and operator= are okay.

  const char* what() const noexcept override
  {
    return message_.c_str();
  }

  const char* stackTrace() const noexcept
  {
    return stack_.c_str();
  }

 private:
  string message_;
  string stack_;
};

}  // namespace muduo

#endif  // MUDUO_BASE_EXCEPTION_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
