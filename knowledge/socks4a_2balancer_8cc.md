---
title: examples/socks4a/balancer.cc

---

# examples/socks4a/balancer.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[onServerConnection](/socks4a_2balancer_8cc.md#function-onserverconnection)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[onServerMessage](/socks4a_2balancer_8cc.md#function-onservermessage)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) ) |
| int | **[main](/socks4a_2balancer_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| std::vector< [InetAddress](/class_inet_address.md) > | **[g_backends](/socks4a_2balancer_8cc.md#variable-g-backends)**  |
| [ThreadLocal](/classmuduo_1_1_thread_local.md)< std::map< string, [TunnelPtr](/tunnel_8h.md#typedef-tunnelptr) > > | **[t_tunnels](/socks4a_2balancer_8cc.md#variable-t-tunnels)**  |
| MutexLock | **[g_mutex](/socks4a_2balancer_8cc.md#variable-g-mutex)**  |
| size_t | **[g_current](/socks4a_2balancer_8cc.md#variable-g-current)**  |


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


### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```



## Attributes Documentation

### variable g_backends

```cpp
std::vector< InetAddress > g_backends;
```


### variable t_tunnels

```cpp
ThreadLocal< std::map< string, TunnelPtr > > t_tunnels;
```


### variable g_mutex

```cpp
MutexLock g_mutex;
```


### variable g_current

```cpp
size_t g_current = 0;
```



## Source code

```cpp
#include "examples/socks4a/tunnel.h"

#include "muduo/base/ThreadLocal.h"
#include <stdio.h>

using namespace muduo;
using namespace muduo::net;

std::vector<InetAddress> g_backends;
ThreadLocal<std::map<string, TunnelPtr> > t_tunnels;
MutexLock g_mutex;
size_t g_current = 0;

void onServerConnection(const TcpConnectionPtr& conn)
{
  LOG_DEBUG << (conn->connected() ? "UP" : "DOWN");
  std::map<string, TunnelPtr>& tunnels = t_tunnels.value();
  if (conn->connected())
  {
    conn->setTcpNoDelay(true);
    conn->stopRead();
    size_t current = 0;
    {
    MutexLockGuard guard(g_mutex);
    current = g_current;
    g_current = (g_current+1) % g_backends.size();
    }

    InetAddress backend = g_backends[current];
    TunnelPtr tunnel(new Tunnel(conn->getLoop(), backend, conn));
    tunnel->setup();
    tunnel->connect();

    tunnels[conn->name()] = tunnel;
  }
  else
  {
    assert(tunnels.find(conn->name()) != tunnels.end());
    tunnels[conn->name()]->disconnect();
    tunnels.erase(conn->name());
  }
}

void onServerMessage(const TcpConnectionPtr& conn, Buffer* buf, Timestamp)
{
  if (!conn->getContext().empty())
  {
    const TcpConnectionPtr& clientConn
      = boost::any_cast<const TcpConnectionPtr&>(conn->getContext());
    clientConn->send(buf);
  }
}

int main(int argc, char* argv[])
{
  if (argc < 3)
  {
    fprintf(stderr, "Usage: %s listen_port backend_ip:port [backend_ip:port]\n", argv[0]);
  }
  else
  {
    for (int i = 2; i < argc; ++i)
    {
      string hostport = argv[i];
      size_t colon = hostport.find(':');
      if (colon != string::npos)
      {
        string ip = hostport.substr(0, colon);
        uint16_t port = static_cast<uint16_t>(atoi(hostport.c_str()+colon+1));
        g_backends.push_back(InetAddress(ip, port));
      }
      else
      {
        fprintf(stderr, "invalid backend address %s\n", argv[i]);
        return 1;
      }
    }

    uint16_t port = static_cast<uint16_t>(atoi(argv[1]));
    InetAddress listenAddr(port);

    EventLoop loop;
    TcpServer server(&loop, listenAddr, "TcpBalancer");
    server.setConnectionCallback(onServerConnection);
    server.setMessageCallback(onServerMessage);
    server.setThreadNum(4);
    server.start();
    loop.loop();
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
