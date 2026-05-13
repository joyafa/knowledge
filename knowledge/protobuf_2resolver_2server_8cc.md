---
title: examples/protobuf/resolver/server.cc

---

# examples/protobuf/resolver/server.cc



## Namespaces

| Name           |
| -------------- |
| **[resolver](/namespaceresolver.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[resolver::ResolverServiceImpl](/classresolver_1_1_resolver_service_impl.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/protobuf_2resolver_2server_8cc.md#function-main)**() |


## Functions Documentation

### function main

```cpp
int main()
```




## Source code

```cpp
#include "examples/protobuf/resolver/resolver.pb.h"

#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/protorpc/RpcServer.h"
#include "examples/cdns/Resolver.h"

#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

namespace resolver
{

class ResolverServiceImpl : public ResolverService
{
 public:
  ResolverServiceImpl(EventLoop* loop)
    : resolver_(loop, cdns::Resolver::kDNSonly)
  {
  }

  virtual void Resolve(::google::protobuf::RpcController* controller,
                       const ::resolver::ResolveRequest* request,
                       ::resolver::ResolveResponse* response,
                       ::google::protobuf::Closure* done)
  {
    LOG_INFO << "ResolverServiceImpl::Resolve " << request->address();

    bool succeed = resolver_.resolve(request->address(),
                                     std::bind(&ResolverServiceImpl::doneCallback,
                                                 this,
                                                 request->address(),
                                                 _1,
                                                 response,
                                                 done));
    if (!succeed)
    {
      response->set_resolved(false);
      done->Run();
    }
  }

 private:

  void doneCallback(const std::string& host,
                    const muduo::net::InetAddress& address,
                    ::resolver::ResolveResponse* response,
                    ::google::protobuf::Closure* done)

  {
    LOG_INFO << "ResolverServiceImpl::doneCallback " << host;
    int32_t ip = address.ipv4NetEndian();
    if (ip)
    {
      response->set_resolved(true);
      response->add_ip(ip);
      response->add_port(address.portNetEndian());
    }
    else
    {
      response->set_resolved(false);
    }
    done->Run();
  }

  cdns::Resolver resolver_;
};

}  // namespace resolver

int main()
{
  LOG_INFO << "pid = " << getpid();
  EventLoop loop;
  InetAddress listenAddr(2053);
  resolver::ResolverServiceImpl impl(&loop);
  RpcServer server(&loop, listenAddr);
  server.registerService(&impl);
  server.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
