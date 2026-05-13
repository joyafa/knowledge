---
title: examples/filetransfer/download3.cc

---

# examples/filetransfer/download3.cc



## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::shared_ptr< FILE > | **[FilePtr](/download3_8cc.md#typedef-fileptr)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[onHighWaterMark](/download3_8cc.md#function-onhighwatermark)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, size_t len) |
| void | **[onConnection](/download3_8cc.md#function-onconnection)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[onWriteComplete](/download3_8cc.md#function-onwritecomplete)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| int | **[main](/download3_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const int | **[kBufSize](/download3_8cc.md#variable-kbufsize)**  |
| const char * | **[g_file](/download3_8cc.md#variable-g-file)**  |

## Types Documentation

### typedef FilePtr

```cpp
typedef std::shared_ptr<FILE> FilePtr;
```



## Functions Documentation

### function onHighWaterMark

```cpp
void onHighWaterMark(
    const TcpConnectionPtr & conn,
    size_t len
)
```


### function onConnection

```cpp
void onConnection(
    const TcpConnectionPtr & conn
)
```


### function onWriteComplete

```cpp
void onWriteComplete(
    const TcpConnectionPtr & conn
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

### variable kBufSize

```cpp
const int kBufSize = 64*1024;
```


### variable g_file

```cpp
const char * g_file = NULL;
```



## Source code

```cpp
#include "muduo/base/Logging.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/TcpServer.h"

#include <stdio.h>
#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

void onHighWaterMark(const TcpConnectionPtr& conn, size_t len)
{
  LOG_INFO << "HighWaterMark " << len;
}

const int kBufSize = 64*1024;
const char* g_file = NULL;
typedef std::shared_ptr<FILE> FilePtr;

void onConnection(const TcpConnectionPtr& conn)
{
  LOG_INFO << "FileServer - " << conn->peerAddress().toIpPort() << " -> "
           << conn->localAddress().toIpPort() << " is "
           << (conn->connected() ? "UP" : "DOWN");
  if (conn->connected())
  {
    LOG_INFO << "FileServer - Sending file " << g_file
             << " to " << conn->peerAddress().toIpPort();
    conn->setHighWaterMarkCallback(onHighWaterMark, kBufSize+1);

    FILE* fp = ::fopen(g_file, "rb");
    if (fp)
    {
      FilePtr ctx(fp, ::fclose);
      conn->setContext(ctx);
      char buf[kBufSize];
      size_t nread = ::fread(buf, 1, sizeof buf, fp);
      conn->send(buf, static_cast<int>(nread));
    }
    else
    {
      conn->shutdown();
      LOG_INFO << "FileServer - no such file";
    }
  }
}

void onWriteComplete(const TcpConnectionPtr& conn)
{
  const FilePtr& fp = boost::any_cast<const FilePtr&>(conn->getContext());
  char buf[kBufSize];
  size_t nread = ::fread(buf, 1, sizeof buf, get_pointer(fp));
  if (nread > 0)
  {
    conn->send(buf, static_cast<int>(nread));
  }
  else
  {
    conn->shutdown();
    LOG_INFO << "FileServer - done";
  }
}

int main(int argc, char* argv[])
{
  LOG_INFO << "pid = " << getpid();
  if (argc > 1)
  {
    g_file = argv[1];

    EventLoop loop;
    InetAddress listenAddr(2021);
    TcpServer server(&loop, listenAddr, "FileServer");
    server.setConnectionCallback(onConnection);
    server.setWriteCompleteCallback(onWriteComplete);
    server.start();
    loop.loop();
  }
  else
  {
    fprintf(stderr, "Usage: %s file_for_downloading\n", argv[0]);
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
