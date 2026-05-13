---
title: examples/socks4a/tcprelay.cc

---

# examples/socks4a/tcprelay.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[onServerConnection](/tcprelay_8cc.md#function-onserverconnection)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[onServerMessage](/tcprelay_8cc.md#function-onservermessage)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) ) |
| void | **[memstat](/tcprelay_8cc.md#function-memstat)**() |
| int | **[main](/tcprelay_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [EventLoop](/class_event_loop.md) * | **[g_eventLoop](/tcprelay_8cc.md#variable-g-eventloop)**  |
| [InetAddress](/class_inet_address.md) * | **[g_serverAddr](/tcprelay_8cc.md#variable-g-serveraddr)**  |
| std::map< string, [TunnelPtr](/tunnel_8h.md#typedef-tunnelptr) > | **[g_tunnels](/tcprelay_8cc.md#variable-g-tunnels)**  |


## Functions Documentation

### function onServerConnection

```cpp
void onServerConnection(
    const TcpConnectionPtr & conn
)
```


### function onServerMessage

```cpp
void onServerMessage(
    const TcpConnectionPtr & conn,
    Buffer * buf,
    Timestamp 
)
```


### function memstat

```cpp
void memstat()
```


### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```



## Attributes Documentation

### variable g_eventLoop

```cpp
EventLoop * g_eventLoop;
```


### variable g_serverAddr

```cpp
InetAddress * g_serverAddr;
```


### variable g_tunnels

```cpp
std::map< string, TunnelPtr > g_tunnels;
```



## Source code

```cpp
#include "examples/socks4a/tunnel.h"

#include <malloc.h>
#include <stdio.h>
#include <sys/resource.h>
#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

EventLoop* g_eventLoop;
InetAddress* g_serverAddr;
std::map<string, TunnelPtr> g_tunnels;

void onServerConnection(const TcpConnectionPtr& conn)
{
  LOG_DEBUG << (conn->connected() ? "UP" : "DOWN");
  if (conn->connected())
  {
    conn->setTcpNoDelay(true);
    conn->stopRead();
    TunnelPtr tunnel(new Tunnel(g_eventLoop, *g_serverAddr, conn));
    tunnel->setup();
    tunnel->connect();
    g_tunnels[conn->name()] = tunnel;
  }
  else
  {
    assert(g_tunnels.find(conn->name()) != g_tunnels.end());
    g_tunnels[conn->name()]->disconnect();
    g_tunnels.erase(conn->name());
  }
}

void onServerMessage(const TcpConnectionPtr& conn, Buffer* buf, Timestamp)
{
  LOG_DEBUG << buf->readableBytes();
  if (!conn->getContext().empty())
  {
    const TcpConnectionPtr& clientConn
      = boost::any_cast<const TcpConnectionPtr&>(conn->getContext());
    clientConn->send(buf);
  }
}

void memstat()
{
  malloc_stats();
}

int main(int argc, char* argv[])
{
  if (argc < 4)
  {
    fprintf(stderr, "Usage: %s <host_ip> <port> <listen_port>\n", argv[0]);
  }
  else
  {
    LOG_INFO << "pid = " << getpid() << ", tid = " << CurrentThread::tid();
    {
      // set max virtual memory to 256MB.
      size_t kOneMB = 1024*1024;
      rlimit rl = { 256*kOneMB, 256*kOneMB };
      setrlimit(RLIMIT_AS, &rl);
    }
    const char* ip = argv[1];
    uint16_t port = static_cast<uint16_t>(atoi(argv[2]));
    InetAddress serverAddr(ip, port);
    g_serverAddr = &serverAddr;

    uint16_t acceptPort = static_cast<uint16_t>(atoi(argv[3]));
    InetAddress listenAddr(acceptPort);

    EventLoop loop;
    g_eventLoop = &loop;
    loop.runEvery(3, memstat);

    TcpServer server(&loop, listenAddr, "TcpRelay");

    server.setConnectionCallback(onServerConnection);
    server.setMessageCallback(onServerMessage);

    server.start();

    loop.loop();
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
