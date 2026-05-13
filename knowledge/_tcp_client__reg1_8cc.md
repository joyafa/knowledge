---
title: muduo/net/tests/TcpClient_reg1.cc

---

# muduo/net/tests/TcpClient_reg1.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[timeout](/_tcp_client__reg1_8cc.md#function-timeout)**() |
| int | **[main](/_tcp_client__reg1_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [TcpClient](/classmuduo_1_1net_1_1_tcp_client.md) * | **[g_client](/_tcp_client__reg1_8cc.md#variable-g-client)**  |


## Functions Documentation

### function timeout

```cpp
void timeout()
```


### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```



## Attributes Documentation

### variable g_client

```cpp
TcpClient * g_client;
```



## Source code

```cpp
// TcpClient::stop() called in the same iteration of IO event

#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/TcpClient.h"

using namespace muduo;
using namespace muduo::net;

TcpClient* g_client;

void timeout()
{
  LOG_INFO << "timeout";
  g_client->stop();
}

int main(int argc, char* argv[])
{
  EventLoop loop;
  InetAddress serverAddr("127.0.0.1", 2); // no such server
  TcpClient client(&loop, serverAddr, "TcpClient");
  g_client = &client;
  loop.runAfter(0.0, timeout);
  loop.runAfter(1.0, std::bind(&EventLoop::quit, &loop));
  client.connect();
  CurrentThread::sleepUsec(100 * 1000);
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
