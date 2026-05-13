---
title: contrib/thrift/ThriftConnection.h

---

# contrib/thrift/ThriftConnection.h



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[ThriftConnection](/class_thrift_connection.md)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef boost::shared_ptr< [ThriftConnection](/class_thrift_connection.md) > | **[ThriftConnectionPtr](/_thrift_connection_8h.md#typedef-thriftconnectionptr)**  |

## Types Documentation

### typedef ThriftConnectionPtr

```cpp
typedef boost::shared_ptr<ThriftConnection> ThriftConnectionPtr;
```





## Source code

```cpp
#ifndef MUDUO_CONTRIB_THRIFT_THRIFTCONNECTION_H
#define MUDUO_CONTRIB_THRIFT_THRIFTCONNECTION_H

#include <boost/enable_shared_from_this.hpp>
#include <boost/noncopyable.hpp>

#include "muduo/net/TcpConnection.h"

#include <thrift/protocol/TProtocol.h>
#include <thrift/transport/TBufferTransports.h>
#include <thrift/transport/TTransportUtils.h>

using apache::thrift::TProcessor;
using apache::thrift::protocol::TProtocol;
using apache::thrift::transport::TMemoryBuffer;
using apache::thrift::transport::TNullTransport;
using apache::thrift::transport::TTransport;
using apache::thrift::transport::TTransportException;

class ThriftServer;

class ThriftConnection : boost::noncopyable,
                         public boost::enable_shared_from_this<ThriftConnection>
{
 public:
  enum State
  {
    kExpectFrameSize,
    kExpectFrame
  };

  ThriftConnection(ThriftServer* server, const muduo::net::TcpConnectionPtr& conn);

 private:
  void onMessage(const muduo::net::TcpConnectionPtr& conn,
                 muduo::net::Buffer* buffer,
                 muduo::Timestamp receiveTime);

  void process();

  void close();

 private:
  ThriftServer* server_;
  muduo::net::TcpConnectionPtr conn_;

  boost::shared_ptr<TNullTransport> nullTransport_;

  boost::shared_ptr<TMemoryBuffer> inputTransport_;
  boost::shared_ptr<TMemoryBuffer> outputTransport_;

  boost::shared_ptr<TTransport> factoryInputTransport_;
  boost::shared_ptr<TTransport> factoryOutputTransport_;

  boost::shared_ptr<TProtocol> inputProtocol_;
  boost::shared_ptr<TProtocol> outputProtocol_;

  boost::shared_ptr<TProcessor> processor_;

  enum State state_;
  uint32_t frameSize_;
};

typedef boost::shared_ptr<ThriftConnection> ThriftConnectionPtr;

#endif  // MUDUO_CONTRIB_THRIFT_THRIFTCONNECTION_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
