---
title: examples/simple/echo/echo.h

---

# examples/simple/echo/echo.h



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[EchoServer](/class_echo_server.md)**  |




## Source code

```cpp
#ifndef MUDUO_EXAMPLES_SIMPLE_ECHO_ECHO_H
#define MUDUO_EXAMPLES_SIMPLE_ECHO_ECHO_H

#include "muduo/net/TcpServer.h"

// RFC 862
class EchoServer
{
 public:
  EchoServer(muduo::net::EventLoop* loop,
             const muduo::net::InetAddress& listenAddr);

  void start();  // calls server_.start();

 private:
  void onConnection(const muduo::net::TcpConnectionPtr& conn);

  void onMessage(const muduo::net::TcpConnectionPtr& conn,
                 muduo::net::Buffer* buf,
                 muduo::Timestamp time);

  muduo::net::TcpServer server_;
};

#endif  // MUDUO_EXAMPLES_SIMPLE_ECHO_ECHO_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
