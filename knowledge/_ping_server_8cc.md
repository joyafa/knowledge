---
title: contrib/thrift/tests/ping/PingServer.cc

---

# contrib/thrift/tests/ping/PingServer.cc



## Namespaces

| Name           |
| -------------- |
| **[ping](/namespaceping.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[PingHandler](/class_ping_handler.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/_ping_server_8cc.md#function-main)**(int argc, char ** argv) |


## Functions Documentation

### function main

```cpp
int main(
    int argc,
    char ** argv
)
```




## Source code

```cpp
#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"

#include <thrift/protocol/TCompactProtocol.h>

#include "ThriftServer.h"

#include "Ping.h"

using namespace muduo;
using namespace muduo::net;

using apache::thrift::protocol::TCompactProtocolFactory;

using namespace ping;

class PingHandler : virtual public PingIf
{
 public:
  PingHandler()
  {
  }

  void ping()
  {
    LOG_INFO << "ping";
  }

};

int main(int argc, char **argv)
{
  EventLoop eventloop;
  InetAddress addr("127.0.0.1", 9090);
  string name("PingServer");

  boost::shared_ptr<PingHandler> handler(new PingHandler());
  boost::shared_ptr<TProcessor> processor(new PingProcessor(handler));
  boost::shared_ptr<TProtocolFactory> protcolFactory(new TCompactProtocolFactory());

  ThriftServer server(processor, protcolFactory, &eventloop, addr, name);
  server.start();
  eventloop.loop();

  return 0;
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
