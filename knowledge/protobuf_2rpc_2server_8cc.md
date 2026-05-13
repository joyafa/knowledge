---
title: examples/protobuf/rpc/server.cc

---

# examples/protobuf/rpc/server.cc



## Namespaces

| Name           |
| -------------- |
| **[sudoku](/namespacesudoku.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[sudoku::SudokuServiceImpl](/classsudoku_1_1_sudoku_service_impl.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/protobuf_2rpc_2server_8cc.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
#include "examples/protobuf/rpc/sudoku.pb.h"

#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/protorpc/RpcServer.h"

#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

namespace sudoku
{

class SudokuServiceImpl : public SudokuService
{
 public:
  virtual void Solve(::google::protobuf::RpcController* controller,
                       const ::sudoku::SudokuRequest* request,
                       ::sudoku::SudokuResponse* response,
                       ::google::protobuf::Closure* done)
  {
    LOG_INFO << "SudokuServiceImpl::Solve";
    response->set_solved(true);
    response->set_checkerboard("1234567");
    done->Run();
  }
};

}  // namespace sudoku

int main()
{
  LOG_INFO << "pid = " << getpid();
  EventLoop loop;
  InetAddress listenAddr(9981);
  sudoku::SudokuServiceImpl impl;
  RpcServer server(&loop, listenAddr);
  server.registerService(&impl);
  server.start();
  loop.loop();
  google::protobuf::ShutdownProtobufLibrary();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
