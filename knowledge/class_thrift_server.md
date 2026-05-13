---
title: ThriftServer

---

# ThriftServer






`#include <ThriftServer.h>`

Inherits from boost::noncopyable, TServer

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ThriftServer](/class_thrift_server.md#function-thriftserver)**(const boost::shared_ptr< TProcessorFactory > & processorFactory, [muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * eventloop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & addr, const muduo::string & name) |
| | **[ThriftServer](/class_thrift_server.md#function-thriftserver)**(const boost::shared_ptr< TProcessor > & processor, [muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * eventloop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & addr, const muduo::string & name) |
| | **[ThriftServer](/class_thrift_server.md#function-thriftserver)**(const boost::shared_ptr< TProcessorFactory > & processorFactory, const boost::shared_ptr< TProtocolFactory > & protocolFactory, [muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * eventloop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & addr, const muduo::string & name) |
| | **[ThriftServer](/class_thrift_server.md#function-thriftserver)**(const boost::shared_ptr< TProcessor > & processor, const boost::shared_ptr< TProtocolFactory > & protocolFactory, [muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * eventloop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & addr, const muduo::string & name) |
| | **[ThriftServer](/class_thrift_server.md#function-thriftserver)**(const boost::shared_ptr< TProcessorFactory > & processorFactory, const boost::shared_ptr< TTransportFactory > & transportFactory, const boost::shared_ptr< TProtocolFactory > & protocolFactory, [muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * eventloop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & addr, const muduo::string & name) |
| | **[ThriftServer](/class_thrift_server.md#function-thriftserver)**(const boost::shared_ptr< TProcessor > & processor, const boost::shared_ptr< TTransportFactory > & transportFactory, const boost::shared_ptr< TProtocolFactory > & protocolFactory, [muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * eventloop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & addr, const muduo::string & name) |
| | **[ThriftServer](/class_thrift_server.md#function-thriftserver)**(const boost::shared_ptr< TProcessorFactory > & processorFactory, const boost::shared_ptr< TTransportFactory > & inputTransportFactory, const boost::shared_ptr< TTransportFactory > & outputTransportFactory, const boost::shared_ptr< TProtocolFactory > & inputProtocolFactory, const boost::shared_ptr< TProtocolFactory > & outputProtocolFactory, [muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * eventloop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & addr, const muduo::string & name) |
| | **[ThriftServer](/class_thrift_server.md#function-thriftserver)**(const boost::shared_ptr< TProcessor > & processor, const boost::shared_ptr< TTransportFactory > & inputTransportFactory, const boost::shared_ptr< TTransportFactory > & outputTransportFactory, const boost::shared_ptr< TProtocolFactory > & inputProtocolFactory, const boost::shared_ptr< TProtocolFactory > & outputProtocolFactory, [muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * eventloop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & addr, const muduo::string & name) |
| virtual | **[~ThriftServer](/class_thrift_server.md#function-~thriftserver)**() |
| void | **[serve](/class_thrift_server.md#function-serve)**() |
| void | **[start](/class_thrift_server.md#function-start)**() |
| void | **[stop](/class_thrift_server.md#function-stop)**() |
| [muduo::ThreadPool](/classmuduo_1_1_thread_pool.md) & | **[workerThreadPool](/class_thrift_server.md#function-workerthreadpool)**() |
| bool | **[isWorkerThreadPoolProcessing](/class_thrift_server.md#function-isworkerthreadpoolprocessing)**() const |
| void | **[setThreadNum](/class_thrift_server.md#function-setthreadnum)**(int numThreads) |
| void | **[setWorkerThreadNum](/class_thrift_server.md#function-setworkerthreadnum)**(int numWorkerThreads) |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[ThriftConnection](/class_thrift_server.md#friend-thriftconnection)**  |

## Public Functions Documentation

### function ThriftServer

```cpp
inline ThriftServer(
    const boost::shared_ptr< TProcessorFactory > & processorFactory,
    muduo::net::EventLoop * eventloop,
    const muduo::net::InetAddress & addr,
    const muduo::string & name
)
```


### function ThriftServer

```cpp
inline ThriftServer(
    const boost::shared_ptr< TProcessor > & processor,
    muduo::net::EventLoop * eventloop,
    const muduo::net::InetAddress & addr,
    const muduo::string & name
)
```


### function ThriftServer

```cpp
inline ThriftServer(
    const boost::shared_ptr< TProcessorFactory > & processorFactory,
    const boost::shared_ptr< TProtocolFactory > & protocolFactory,
    muduo::net::EventLoop * eventloop,
    const muduo::net::InetAddress & addr,
    const muduo::string & name
)
```


### function ThriftServer

```cpp
inline ThriftServer(
    const boost::shared_ptr< TProcessor > & processor,
    const boost::shared_ptr< TProtocolFactory > & protocolFactory,
    muduo::net::EventLoop * eventloop,
    const muduo::net::InetAddress & addr,
    const muduo::string & name
)
```


### function ThriftServer

```cpp
inline ThriftServer(
    const boost::shared_ptr< TProcessorFactory > & processorFactory,
    const boost::shared_ptr< TTransportFactory > & transportFactory,
    const boost::shared_ptr< TProtocolFactory > & protocolFactory,
    muduo::net::EventLoop * eventloop,
    const muduo::net::InetAddress & addr,
    const muduo::string & name
)
```


### function ThriftServer

```cpp
inline ThriftServer(
    const boost::shared_ptr< TProcessor > & processor,
    const boost::shared_ptr< TTransportFactory > & transportFactory,
    const boost::shared_ptr< TProtocolFactory > & protocolFactory,
    muduo::net::EventLoop * eventloop,
    const muduo::net::InetAddress & addr,
    const muduo::string & name
)
```


### function ThriftServer

```cpp
inline ThriftServer(
    const boost::shared_ptr< TProcessorFactory > & processorFactory,
    const boost::shared_ptr< TTransportFactory > & inputTransportFactory,
    const boost::shared_ptr< TTransportFactory > & outputTransportFactory,
    const boost::shared_ptr< TProtocolFactory > & inputProtocolFactory,
    const boost::shared_ptr< TProtocolFactory > & outputProtocolFactory,
    muduo::net::EventLoop * eventloop,
    const muduo::net::InetAddress & addr,
    const muduo::string & name
)
```


### function ThriftServer

```cpp
inline ThriftServer(
    const boost::shared_ptr< TProcessor > & processor,
    const boost::shared_ptr< TTransportFactory > & inputTransportFactory,
    const boost::shared_ptr< TTransportFactory > & outputTransportFactory,
    const boost::shared_ptr< TProtocolFactory > & inputProtocolFactory,
    const boost::shared_ptr< TProtocolFactory > & outputProtocolFactory,
    muduo::net::EventLoop * eventloop,
    const muduo::net::InetAddress & addr,
    const muduo::string & name
)
```


### function ~ThriftServer

```cpp
virtual ~ThriftServer()
```


### function serve

```cpp
void serve()
```


### function start

```cpp
void start()
```


### function stop

```cpp
void stop()
```


### function workerThreadPool

```cpp
inline muduo::ThreadPool & workerThreadPool()
```


### function isWorkerThreadPoolProcessing

```cpp
inline bool isWorkerThreadPoolProcessing() const
```


### function setThreadNum

```cpp
inline void setThreadNum(
    int numThreads
)
```


### function setWorkerThreadNum

```cpp
inline void setWorkerThreadNum(
    int numWorkerThreads
)
```


## Friends

### friend ThriftConnection

```cpp
friend class ThriftConnection(
    ThriftConnection 
);
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800