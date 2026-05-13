---
title: muduo/net/protorpc/RpcServer.h

---

# muduo/net/protorpc/RpcServer.h



## Namespaces

| Name           |
| -------------- |
| **[google](/namespacegoogle.md)**  |
| **[google::protobuf](/namespacegoogle_1_1protobuf.md)**  |
| **[muduo](/namespacemuduo.md)**  |
| **[muduo::net](/namespacemuduo_1_1net.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::net::RpcServer](/classmuduo_1_1net_1_1_rpc_server.md)**  |




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

#ifndef MUDUO_NET_PROTORPC_RPCSERVER_H
#define MUDUO_NET_PROTORPC_RPCSERVER_H

#include "muduo/net/TcpServer.h"

namespace google {
namespace protobuf {

class Service;

}  // namespace protobuf
}  // namespace google

namespace muduo
{
namespace net
{

class RpcServer
{
 public:
  RpcServer(EventLoop* loop,
            const InetAddress& listenAddr);

  void setThreadNum(int numThreads)
  {
    server_.setThreadNum(numThreads);
  }

  void registerService(::google::protobuf::Service*);
  void start();

 private:
  void onConnection(const TcpConnectionPtr& conn);

  // void onMessage(const TcpConnectionPtr& conn,
  //                Buffer* buf,
  //                Timestamp time);

  TcpServer server_;
  std::map<std::string, ::google::protobuf::Service*> services_;
};

}  // namespace net
}  // namespace muduo

#endif  // MUDUO_NET_PROTORPC_RPCSERVER_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
