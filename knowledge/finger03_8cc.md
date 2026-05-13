---
title: examples/twisted/finger/finger03.cc

---

# examples/twisted/finger/finger03.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[onConnection](/finger03_8cc.md#function-onconnection)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| int | **[main](/finger03_8cc.md#function-main)**() |


## Functions Documentation

### function onConnection

```cpp
void onConnection(
    const TcpConnectionPtr & conn
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

void onConnection(const TcpConnectionPtr& conn)
{
  if (conn->connected())
  {
    conn->shutdown();
  }
}

int main()
{
  EventLoop loop;
  TcpServer server(&loop, InetAddress(1079), "Finger");
  server.setConnectionCallback(onConnection);
  server.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
