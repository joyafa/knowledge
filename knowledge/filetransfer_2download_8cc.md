---
title: examples/filetransfer/download.cc

---

# examples/filetransfer/download.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| string | **[readFile](/filetransfer_2download_8cc.md#function-readfile)**(const char * filename) |
| void | **[onHighWaterMark](/filetransfer_2download_8cc.md#function-onhighwatermark)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, size_t len) |
| void | **[onConnection](/filetransfer_2download_8cc.md#function-onconnection)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| int | **[main](/filetransfer_2download_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const char * | **[g_file](/filetransfer_2download_8cc.md#variable-g-file)**  |


## Functions Documentation

### function readFile

```cpp
string readFile(
    const char * filename
)
```


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


### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```



## Attributes Documentation

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

const char* g_file = NULL;

// FIXME: use FileUtil::readFile()
string readFile(const char* filename)
{
  string content;
  FILE* fp = ::fopen(filename, "rb");
  if (fp)
  {
    // inefficient!!!
    const int kBufSize = 1024*1024;
    char iobuf[kBufSize];
    ::setbuffer(fp, iobuf, sizeof iobuf);

    char buf[kBufSize];
    size_t nread = 0;
    while ( (nread = ::fread(buf, 1, sizeof buf, fp)) > 0)
    {
      content.append(buf, nread);
    }
    ::fclose(fp);
  }
  return content;
}

void onHighWaterMark(const TcpConnectionPtr& conn, size_t len)
{
  LOG_INFO << "HighWaterMark " << len;
}

void onConnection(const TcpConnectionPtr& conn)
{
  LOG_INFO << "FileServer - " << conn->peerAddress().toIpPort() << " -> "
           << conn->localAddress().toIpPort() << " is "
           << (conn->connected() ? "UP" : "DOWN");
  if (conn->connected())
  {
    LOG_INFO << "FileServer - Sending file " << g_file
             << " to " << conn->peerAddress().toIpPort();
    conn->setHighWaterMarkCallback(onHighWaterMark, 64*1024);
    string fileContent = readFile(g_file);
    conn->send(fileContent);
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
