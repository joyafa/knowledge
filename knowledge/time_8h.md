---
title: examples/simple/time/time.h

---

# examples/simple/time/time.h



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[TimeServer](/class_time_server.md)**  |




## Source code

```cpp
#ifndef MUDUO_EXAMPLES_SIMPLE_TIME_TIME_H
#define MUDUO_EXAMPLES_SIMPLE_TIME_TIME_H

#include "muduo/net/TcpServer.h"

// RFC 868
class TimeServer
{
 public:
  TimeServer(muduo::net::EventLoop* loop,
             const muduo::net::InetAddress& listenAddr);

  void start();

 private:
  void onConnection(const muduo::net::TcpConnectionPtr& conn);

  void onMessage(const muduo::net::TcpConnectionPtr& conn,
                 muduo::net::Buffer* buf,
                 muduo::Timestamp time);

  muduo::net::TcpServer server_;
};

#endif  // MUDUO_EXAMPLES_SIMPLE_TIME_TIME_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
