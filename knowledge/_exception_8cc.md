---
title: muduo/base/Exception.cc

---

# muduo/base/Exception.cc



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |




## Source code

```cpp
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.
//
// Author: Shuo Chen (chenshuo at chenshuo dot com)

#include "muduo/base/Exception.h"
#include "muduo/base/CurrentThread.h"

namespace muduo
{

Exception::Exception(string msg)
  : message_(std::move(msg)),
    stack_(CurrentThread::stackTrace(/*demangle=*/false))
{
}

}  // namespace muduo
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
