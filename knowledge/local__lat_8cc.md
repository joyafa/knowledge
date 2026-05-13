---
title: examples/zeromq/local_lat.cc

---

# examples/zeromq/local_lat.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[onConnection](/local__lat_8cc.md#function-onconnection)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[onStringMessage](/local__lat_8cc.md#function-onstringmessage)**([LengthHeaderCodec](/class_length_header_codec.md) * codec, const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, const muduo::string & message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) ) |
| int | **[main](/local__lat_8cc.md#function-main)**(int argc, char * argv[]) |
| template <typename T \> <br>T * | **[get_pointer](/local__lat_8cc.md#function-get-pointer)**(const std::shared_ptr< T > & ptr) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[g_tcpNoDelay](/local__lat_8cc.md#variable-g-tcpnodelay)**  |


## Functions Documentation

### function onConnection

```cpp
void onConnection(
    const muduo::net::TcpConnectionPtr & conn
)
```


### function onStringMessage

```cpp
void onStringMessage(
    LengthHeaderCodec * codec,
    const muduo::net::TcpConnectionPtr & conn,
    const muduo::string & message,
    muduo::Timestamp 
)
```


### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```


### function get_pointer

```cpp
template <typename T >
inline T * get_pointer(
    const std::shared_ptr< T > & ptr
)
```



## Attributes Documentation

### variable g_tcpNoDelay

```cpp
bool g_tcpNoDelay = false;
```



## Source code

```cpp
#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/TcpServer.h"
#include "examples/asio/chat/codec.h"

#include <stdio.h>
#include <unistd.h>

using std::placeholders::_1;
using std::placeholders::_2;
using std::placeholders::_3;
using muduo::get_pointer;

bool g_tcpNoDelay = false;

void onConnection(const muduo::net::TcpConnectionPtr& conn)
{
  if (conn->connected())
  {
    conn->setTcpNoDelay(g_tcpNoDelay);
  }
}

void onStringMessage(LengthHeaderCodec* codec,
                     const muduo::net::TcpConnectionPtr& conn,
                     const muduo::string& message,
                     muduo::Timestamp)
{
  codec->send(get_pointer(conn), message);
}

int main(int argc, char* argv[])
{
  if (argc > 1)
  {
    uint16_t port = static_cast<uint16_t>(atoi(argv[1]));
    g_tcpNoDelay = argc > 2 ? atoi(argv[2]) : false;
    int threadCount = argc > 3 ? atoi(argv[3]) : 0;

    LOG_INFO << "pid = " << getpid() << ", listen port = " << port;
    // muduo::Logger::setLogLevel(muduo::Logger::WARN);
    muduo::net::EventLoop loop;
    muduo::net::InetAddress listenAddr(port);
    muduo::net::TcpServer server(&loop, listenAddr, "PingPong");
    LengthHeaderCodec codec(std::bind(onStringMessage, &codec, _1, _2, _3));

    server.setConnectionCallback(onConnection);
    server.setMessageCallback(
        std::bind(&LengthHeaderCodec::onMessage, &codec, _1, _2, _3));

    if (threadCount > 1)
    {
      server.setThreadNum(threadCount);
    }

    server.start();

    loop.loop();
  }
  else
  {
    fprintf(stderr, "Usage: %s listen_port [tcp_no_delay [threads]]\n", argv[0]);
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
