---
title: contrib/thrift/ThriftServer.cc

---

# contrib/thrift/ThriftServer.cc



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[MutexLockGuard](/class_mutex_lock_guard.md)**  |
| class | **[EventLoop](/class_event_loop.md)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::shared_ptr< TcpConnection > | **[TcpConnectionPtr](/_thrift_server_8cc.md#typedef-tcpconnectionptr)**  |

## Types Documentation

### typedef TcpConnectionPtr

```cpp
typedef std::shared_ptr< TcpConnection > muduo::net::TcpConnectionPtr;
```





## Source code

```cpp
#include "contrib/thrift/ThriftServer.h"

#include <functional>

#include "muduo/net/EventLoop.h"

using muduo::MutexLockGuard;
using muduo::Timestamp;
using muduo::net::EventLoop;
using muduo::net::TcpConnectionPtr;

ThriftServer::~ThriftServer() = default;

void ThriftServer::serve()
{
  start();
}

void ThriftServer::start()
{
  if (numWorkerThreads_ > 0)
  {
    workerThreadPool_.start(numWorkerThreads_);
  }
  server_.start();
}

void ThriftServer::stop()
{
  if (numWorkerThreads_ > 0)
  {
    workerThreadPool_.stop();
  }
  server_.getLoop()->runAfter(3.0, std::bind(&EventLoop::quit,
                                               server_.getLoop()));
}

void ThriftServer::onConnection(const TcpConnectionPtr& conn)
{
  if (conn->connected())
  {
    ThriftConnectionPtr ptr(new ThriftConnection(this, conn));
    MutexLockGuard lock(mutex_);
    assert(conns_.find(conn->name()) == conns_.end());
    conns_[conn->name()] = ptr;
  }
  else
  {
    MutexLockGuard lock(mutex_);
    assert(conns_.find(conn->name()) != conns_.end());
    conns_.erase(conn->name());
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
