---
title: muduo/net/tests/TcpClient_reg2.cc

---

# muduo/net/tests/TcpClient_reg2.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[threadFunc](/_tcp_client__reg2_8cc.md#function-threadfunc)**([EventLoop](/class_event_loop.md) * loop) |
| int | **[main](/_tcp_client__reg2_8cc.md#function-main)**(int argc, char * argv[]) |


## Functions Documentation

### function threadFunc

```cpp
void threadFunc(
    EventLoop * loop
)
```


### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```




## Source code

```cpp
// TcpClient destructs when TcpConnection is connected but unique.

#include "muduo/base/Logging.h"
#include "muduo/base/Thread.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/TcpClient.h"

using namespace muduo;
using namespace muduo::net;

void threadFunc(EventLoop* loop)
{
  InetAddress serverAddr("127.0.0.1", 1234); // should succeed
  TcpClient client(loop, serverAddr, "TcpClient");
  client.connect();

  CurrentThread::sleepUsec(1000*1000);
  // client destructs when connected.
}

int main(int argc, char* argv[])
{
  Logger::setLogLevel(Logger::DEBUG);

  EventLoop loop;
  loop.runAfter(3.0, std::bind(&EventLoop::quit, &loop));
  Thread thr(std::bind(threadFunc, &loop));
  thr.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
