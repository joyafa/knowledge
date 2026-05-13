---
title: muduo/net/tests/EchoClient_unittest.cc

---

# muduo/net/tests/EchoClient_unittest.cc



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[EchoClient](/class_echo_client.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/_echo_client__unittest_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[numThreads](/_echo_client__unittest_8cc.md#variable-numthreads)**  |
| std::vector< std::unique_ptr< [EchoClient](/class_echo_client.md) > > | **[clients](/_echo_client__unittest_8cc.md#variable-clients)**  |
| int | **[current](/_echo_client__unittest_8cc.md#variable-current)**  |


## Functions Documentation

### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```



## Attributes Documentation

### variable numThreads

```cpp
int numThreads = 0;
```


### variable clients

```cpp
std::vector< std::unique_ptr< EchoClient > > clients;
```


### variable current

```cpp
int current = 0;
```



## Source code

```cpp
#include "muduo/net/TcpClient.h"

#include "muduo/base/Logging.h"
#include "muduo/base/Thread.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/InetAddress.h"

#include <utility>

#include <stdio.h>
#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

int numThreads = 0;
class EchoClient;
std::vector<std::unique_ptr<EchoClient>> clients;
int current = 0;

class EchoClient : noncopyable
{
 public:
  EchoClient(EventLoop* loop, const InetAddress& listenAddr, const string& id)
    : loop_(loop),
      client_(loop, listenAddr, "EchoClient"+id)
  {
    client_.setConnectionCallback(
        std::bind(&EchoClient::onConnection, this, _1));
    client_.setMessageCallback(
        std::bind(&EchoClient::onMessage, this, _1, _2, _3));
    //client_.enableRetry();
  }

  void connect()
  {
    client_.connect();
  }
  // void stop();

 private:
  void onConnection(const TcpConnectionPtr& conn)
  {
    LOG_TRACE << conn->localAddress().toIpPort() << " -> "
        << conn->peerAddress().toIpPort() << " is "
        << (conn->connected() ? "UP" : "DOWN");

    if (conn->connected())
    {
      ++current;
      if (implicit_cast<size_t>(current) < clients.size())
      {
        clients[current]->connect();
      }
      LOG_INFO << "*** connected " << current;
    }
    conn->send("world\n");
  }

  void onMessage(const TcpConnectionPtr& conn, Buffer* buf, Timestamp time)
  {
    string msg(buf->retrieveAllAsString());
    LOG_TRACE << conn->name() << " recv " << msg.size() << " bytes at " << time.toString();
    if (msg == "quit\n")
    {
      conn->send("bye\n");
      conn->shutdown();
    }
    else if (msg == "shutdown\n")
    {
      loop_->quit();
    }
    else
    {
      conn->send(msg);
    }
  }

  EventLoop* loop_;
  TcpClient client_;
};

int main(int argc, char* argv[])
{
  LOG_INFO << "pid = " << getpid() << ", tid = " << CurrentThread::tid();
  if (argc > 1)
  {
    EventLoop loop;
    bool ipv6 = argc > 3;
    InetAddress serverAddr(argv[1], 2000, ipv6);

    int n = 1;
    if (argc > 2)
    {
      n = atoi(argv[2]);
    }

    clients.reserve(n);
    for (int i = 0; i < n; ++i)
    {
      char buf[32];
      snprintf(buf, sizeof buf, "%d", i+1);
      clients.emplace_back(new EchoClient(&loop, serverAddr, buf));
    }

    clients[current]->connect();
    loop.loop();
  }
  else
  {
    printf("Usage: %s host_ip [current#]\n", argv[0]);
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
