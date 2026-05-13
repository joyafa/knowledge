---
title: muduo/net/Socket.h

---

# muduo/net/Socket.h



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |
| **[muduo::net](/namespacemuduo_1_1net.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::net::Socket](/classmuduo_1_1net_1_1_socket.md)**  |




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

#ifndef MUDUO_NET_SOCKET_H
#define MUDUO_NET_SOCKET_H

#include "muduo/base/noncopyable.h"

// struct tcp_info is in <netinet/tcp.h>
struct tcp_info;

namespace muduo
{
namespace net
{

class InetAddress;

class Socket : noncopyable
{
 public:
  explicit Socket(int sockfd)
    : sockfd_(sockfd)
  { }

  // Socket(Socket&&) // move constructor in C++11
  ~Socket();

  int fd() const { return sockfd_; }
  // return true if success.
  bool getTcpInfo(struct tcp_info*) const;
  bool getTcpInfoString(char* buf, int len) const;

  void bindAddress(const InetAddress& localaddr);
  void listen();

  int accept(InetAddress* peeraddr);

  void shutdownWrite();

  void setTcpNoDelay(bool on);

  void setReuseAddr(bool on);

  void setReusePort(bool on);

  void setKeepAlive(bool on);

 private:
  const int sockfd_;
};

}  // namespace net
}  // namespace muduo

#endif  // MUDUO_NET_SOCKET_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
