---
title: examples/zeromq/remote_lat.cc

---

# examples/zeromq/remote_lat.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[onConnection](/remote__lat_8cc.md#function-onconnection)**([LengthHeaderCodec](/class_length_header_codec.md) * codec, const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[onStringMessage](/remote__lat_8cc.md#function-onstringmessage)**([LengthHeaderCodec](/class_length_header_codec.md) * codec, const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, const muduo::string & message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) ) |
| int | **[main](/remote__lat_8cc.md#function-main)**(int argc, char * argv[]) |
| template <typename T \> <br>T * | **[get_pointer](/remote__lat_8cc.md#function-get-pointer)**(const std::shared_ptr< T > & ptr) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| bool | **[g_tcpNoDelay](/remote__lat_8cc.md#variable-g-tcpnodelay)**  |
| int | **[g_msgSize](/remote__lat_8cc.md#variable-g-msgsize)**  |
| int | **[g_totalMsgs](/remote__lat_8cc.md#variable-g-totalmsgs)**  |
| int | **[g_msgCount](/remote__lat_8cc.md#variable-g-msgcount)**  |
| muduo::string | **[g_message](/remote__lat_8cc.md#variable-g-message)**  |
| [muduo::Timestamp](/classmuduo_1_1_timestamp.md) | **[g_start](/remote__lat_8cc.md#variable-g-start)**  |


## Functions Documentation

### function onConnection

```cpp
void onConnection(
    LengthHeaderCodec * codec,
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


### variable g_msgSize

```cpp
int g_msgSize = 0;
```


### variable g_totalMsgs

```cpp
int g_totalMsgs = 0;
```


### variable g_msgCount

```cpp
int g_msgCount = 0;
```


### variable g_message

```cpp
muduo::string g_message;
```


### variable g_start

```cpp
muduo::Timestamp g_start;
```



## Source code

```cpp
#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/TcpClient.h"
#include "examples/asio/chat/codec.h"

#include <stdio.h>

using std::placeholders::_1;
using std::placeholders::_2;
using std::placeholders::_3;
using muduo::get_pointer;

bool g_tcpNoDelay = false;
int g_msgSize = 0;
int g_totalMsgs = 0;
int g_msgCount = 0;
muduo::string g_message;
muduo::Timestamp g_start;

void onConnection(LengthHeaderCodec* codec, const muduo::net::TcpConnectionPtr& conn)
{
  if (conn->connected())
  {
    LOG_INFO << "connected";
    g_start = muduo::Timestamp::now();
    conn->setTcpNoDelay(g_tcpNoDelay);
    codec->send(get_pointer(conn), g_message);
  }
  else
  {
    LOG_INFO << "disconnected";
    muduo::net::EventLoop::getEventLoopOfCurrentThread()->quit();
  }
}

void onStringMessage(LengthHeaderCodec* codec,
                     const muduo::net::TcpConnectionPtr& conn,
                     const muduo::string& message,
                     muduo::Timestamp)
{
  if (message.size() != static_cast<size_t>(g_msgSize))
  {
    abort();
  }

  ++g_msgCount;

  if (g_msgCount < g_totalMsgs)
  {
    codec->send(get_pointer(conn), message);
  }
  else
  {
    muduo::Timestamp end = muduo::Timestamp::now();
    LOG_INFO << "done";
    double elapsed = timeDifference(end, g_start);
    LOG_INFO << g_msgSize << " message bytes";
    LOG_INFO << g_msgCount << " round-trips";
    LOG_INFO << elapsed << " seconds";
    LOG_INFO << muduo::Fmt("%.3f", g_msgCount / elapsed) << " round-trips per second";
    LOG_INFO << muduo::Fmt("%.3f", (1000000 * elapsed / g_msgCount / 2))
             << " latency [us]";
    LOG_INFO << muduo::Fmt("%.3f", (g_msgSize * g_msgCount / elapsed / 1024 / 1024))
             << " band width [MiB/s]";
    conn->shutdown();
  }
}

int main(int argc, char* argv[])
{
  if (argc > 3)
  {
    const char* ip = argv[1];
    uint16_t port = static_cast<uint16_t>(atoi(argv[2]));
    g_msgSize = atoi(argv[3]);
    g_message.assign(g_msgSize, 'H');
    g_totalMsgs = argc > 4 ? atoi(argv[4]) : 10000;
    g_tcpNoDelay = argc > 5 ? atoi(argv[5]) : false;

    muduo::net::EventLoop loop;
    muduo::net::InetAddress serverAddr(ip, port);
    muduo::net::TcpClient client(&loop, serverAddr, "Client");
    LengthHeaderCodec codec(std::bind(onStringMessage, &codec, _1, _2, _3));
    client.setConnectionCallback(
        std::bind(onConnection, &codec, _1));
    client.setMessageCallback(
        std::bind(&LengthHeaderCodec::onMessage, &codec, _1, _2, _3));
    client.connect();
    loop.loop();
  }
  else
  {
    fprintf(stderr, "Usage: %s server_ip server_port msg_size", argv[0]);
    fprintf(stderr, " [msg_count [tcp_no_delay]]\n");
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
