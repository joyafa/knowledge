---
title: contrib/thrift/tests/echo/EchoServer.cc

---

# contrib/thrift/tests/echo/EchoServer.cc



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[EchoHandler](/class_echo_handler.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[NumCPU](/_echo_server_8cc.md#function-numcpu)**() |
| int | **[main](/_echo_server_8cc.md#function-main)**(int argc, char ** argv) |


## Functions Documentation

### function NumCPU

```cpp
int NumCPU()
```


### function main

```cpp
int main(
    int argc,
    char ** argv
)
```




## Source code

```cpp
#include <unistd.h>

#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"

#include "ThriftServer.h"

#include "Echo.h"

using namespace muduo;
using namespace muduo::net;

using namespace echo;

class EchoHandler : virtual public EchoIf
{
 public:
  EchoHandler()
  {
  }

  void echo(std::string& str, const std::string& s)
  {
    LOG_INFO << "EchoHandler::echo:" << s;
    str = s;
  }

};

int NumCPU()
{
  return static_cast<int>(sysconf(_SC_NPROCESSORS_ONLN));
}

int main(int argc, char **argv)
{
  EventLoop eventloop;
  InetAddress addr("127.0.0.1", 9090);
  string name("EchoServer");

  boost::shared_ptr<EchoHandler> handler(new EchoHandler());
  boost::shared_ptr<TProcessor> processor(new EchoProcessor(handler));

  ThriftServer server(processor, &eventloop, addr, name);
  server.setWorkerThreadNum(NumCPU() * 2);
  server.start();
  eventloop.loop();

  return 0;
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
