---
title: examples/twisted/finger/finger04.cc

---

# examples/twisted/finger/finger04.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[onMessage](/finger04_8cc.md#function-onmessage)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) receiveTime) |
| int | **[main](/finger04_8cc.md#function-main)**() |


## Functions Documentation

### function onMessage

```cpp
void onMessage(
    const TcpConnectionPtr & conn,
    Buffer * buf,
    Timestamp receiveTime
)
```


### function main

```cpp
int main()
```




## Source code

```cpp
#include "muduo/net/EventLoop.h"
#include "muduo/net/TcpServer.h"

using namespace muduo;
using namespace muduo::net;

void onMessage(const TcpConnectionPtr& conn,
               Buffer* buf,
               Timestamp receiveTime)
{
  if (buf->findCRLF())
  {
    conn->shutdown();
  }
}

int main()
{
  EventLoop loop;
  TcpServer server(&loop, InetAddress(1079), "Finger");
  server.setMessageCallback(onMessage);
  server.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
