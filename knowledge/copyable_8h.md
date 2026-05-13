---
title: muduo/base/copyable.h

---

# muduo/base/copyable.h



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::copyable](/classmuduo_1_1copyable.md)**  |




## Source code

```cpp
#ifndef MUDUO_BASE_COPYABLE_H
#define MUDUO_BASE_COPYABLE_H

namespace muduo
{

class copyable
{
 protected:
  copyable() = default;
  ~copyable() = default;
};

}  // namespace muduo

#endif  // MUDUO_BASE_COPYABLE_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
