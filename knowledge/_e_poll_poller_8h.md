---
title: muduo/net/poller/EPollPoller.h

---

# muduo/net/poller/EPollPoller.h



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |
| **[muduo::net](/namespacemuduo_1_1net.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::net::EPollPoller](/classmuduo_1_1net_1_1_e_poll_poller.md)**  |




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

#ifndef MUDUO_NET_POLLER_EPOLLPOLLER_H
#define MUDUO_NET_POLLER_EPOLLPOLLER_H

#include "muduo/net/Poller.h"

#include <vector>

struct epoll_event;

namespace muduo
{
namespace net
{

class EPollPoller : public Poller
{
 public:
  EPollPoller(EventLoop* loop);
  ~EPollPoller() override;

  Timestamp poll(int timeoutMs, ChannelList* activeChannels) override;
  void updateChannel(Channel* channel) override;
  void removeChannel(Channel* channel) override;

 private:
  static const int kInitEventListSize = 16;

  static const char* operationToString(int op);

  void fillActiveChannels(int numEvents,
                          ChannelList* activeChannels) const;
  void update(int operation, Channel* channel);

  typedef std::vector<struct epoll_event> EventList;

  int epollfd_;
  EventList events_;
};

}  // namespace net
}  // namespace muduo
#endif  // MUDUO_NET_POLLER_EPOLLPOLLER_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
