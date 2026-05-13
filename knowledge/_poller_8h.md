---
title: muduo/net/Poller.h

---

# muduo/net/Poller.h



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |
| **[muduo::net](/namespacemuduo_1_1net.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::net::Poller](/classmuduo_1_1net_1_1_poller.md)**  |




## Source code

```cpp
// Copyright 2010, Shuo Chen.  All rights reserved.
// http://code.google.com/p/muduo/
//
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.

// Author: Shuo Chen (chenshuo at chenshuo dot com)
//
// This is an internal header file, you should not include this.

#ifndef MUDUO_NET_POLLER_H
#define MUDUO_NET_POLLER_H

#include <map>
#include <vector>

#include "muduo/base/Timestamp.h"
#include "muduo/net/EventLoop.h"

namespace muduo
{
namespace net
{

class Channel;

class Poller : noncopyable
{
 public:
  typedef std::vector<Channel*> ChannelList;

  Poller(EventLoop* loop);
  virtual ~Poller();

  virtual Timestamp poll(int timeoutMs, ChannelList* activeChannels) = 0;

  virtual void updateChannel(Channel* channel) = 0;

  virtual void removeChannel(Channel* channel) = 0;

  virtual bool hasChannel(Channel* channel) const;

  static Poller* newDefaultPoller(EventLoop* loop);

  void assertInLoopThread() const
  {
    ownerLoop_->assertInLoopThread();
  }

 protected:
  typedef std::map<int, Channel*> ChannelMap;
  ChannelMap channels_;

 private:
  EventLoop* ownerLoop_;
};

}  // namespace net
}  // namespace muduo

#endif  // MUDUO_NET_POLLER_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
