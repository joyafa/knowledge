---
title: muduo/net/EventLoopThread.h

---

# muduo/net/EventLoopThread.h



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |
| **[muduo::net](/namespacemuduo_1_1net.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::net::EventLoopThread](/classmuduo_1_1net_1_1_event_loop_thread.md)**  |




## Source code

```cpp
// Copyright 2010, Shuo Chen.  All rights reserved.
// http://code.google.com/p/muduo/
//
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.

// Author: Shuo Chen (chenshuo at chenshuo dot com)
//
// This is a public header file, it must only include public header files.

#ifndef MUDUO_NET_EVENTLOOPTHREAD_H
#define MUDUO_NET_EVENTLOOPTHREAD_H

#include "muduo/base/Condition.h"
#include "muduo/base/Mutex.h"
#include "muduo/base/Thread.h"

namespace muduo
{
namespace net
{

class EventLoop;

class EventLoopThread : noncopyable
{
 public:
  typedef std::function<void(EventLoop*)> ThreadInitCallback;

  EventLoopThread(const ThreadInitCallback& cb = ThreadInitCallback(),
                  const string& name = string());
  ~EventLoopThread();
  EventLoop* startLoop();

 private:
  void threadFunc();

  EventLoop* loop_ GUARDED_BY(mutex_);
  bool exiting_;
  Thread thread_;
  MutexLock mutex_;
  Condition cond_ GUARDED_BY(mutex_);
  ThreadInitCallback callback_;
};

}  // namespace net
}  // namespace muduo

#endif  // MUDUO_NET_EVENTLOOPTHREAD_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
