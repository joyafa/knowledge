---
title: examples/twisted/finger/finger07.cc

---

# examples/twisted/finger/finger07.cc



## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::map< string, string > | **[UserMap](/finger07_8cc.md#typedef-usermap)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| string | **[getUser](/finger07_8cc.md#function-getuser)**(const string & user) |
| void | **[onMessage](/finger07_8cc.md#function-onmessage)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) receiveTime) |
| int | **[main](/finger07_8cc.md#function-main)**() |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [UserMap](/finger06_8cc.md#typedef-usermap) | **[users](/finger07_8cc.md#variable-users)**  |

## Types Documentation

### typedef UserMap

```cpp
typedef std::map<string, string> UserMap;
```



## Functions Documentation

### function getUser

```cpp
string getUser(
    const string & user
)
```


### function onMessage

```cpp
void onMessage(
    const TcpConnectionPtr & conn,
    Buffer * buf,
    Timestamp receiveTime
)
```


### function main

```cpp
int main()
```



## Attributes Documentation

### variable users

```cpp
UserMap users;
```



## Source code

```cpp
#include "muduo/net/EventLoop.h"
#include "muduo/net/TcpServer.h"

#include <map>

using namespace muduo;
using namespace muduo::net;

typedef std::map<string, string> UserMap;
UserMap users;

string getUser(const string& user)
{
  string result = "No such user";
  UserMap::iterator it = users.find(user);
  if (it != users.end())
  {
    result = it->second;
  }
  return result;
}

void onMessage(const TcpConnectionPtr& conn,
               Buffer* buf,
               Timestamp receiveTime)
{
  const char* crlf = buf->findCRLF();
  if (crlf)
  {
    string user(buf->peek(), crlf);
    conn->send(getUser(user) + "\r\n");
    buf->retrieveUntil(crlf + 2);
    conn->shutdown();
  }
}

int main()
{
  users["schen"] = "Happy and well";
  EventLoop loop;
  TcpServer server(&loop, InetAddress(1079), "Finger");
  server.setMessageCallback(onMessage);
  server.start();
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
