---
title: muduo/base/noncopyable.h

---

# muduo/base/noncopyable.h



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::noncopyable](/classmuduo_1_1noncopyable.md)**  |




## Source code

```cpp
#ifndef MUDUO_BASE_NONCOPYABLE_H
#define MUDUO_BASE_NONCOPYABLE_H

namespace muduo
{

class noncopyable
{
 public:
  noncopyable(const noncopyable&) = delete;
  void operator=(const noncopyable&) = delete;

 protected:
  noncopyable() = default;
  ~noncopyable() = default;
};

}  // namespace muduo

#endif  // MUDUO_BASE_NONCOPYABLE_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
