---
title: examples/hub/pub.cc

---

# examples/hub/pub.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[connection](/pub_8cc.md#function-connection)**([PubSubClient](/classpubsub_1_1_pub_sub_client.md) * client) |
| int | **[main](/pub_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [EventLoop](/class_event_loop.md) * | **[g_loop](/pub_8cc.md#variable-g-loop)**  |
| string | **[g_topic](/pub_8cc.md#variable-g-topic)**  |
| string | **[g_content](/pub_8cc.md#variable-g-content)**  |


## Functions Documentation

### function connection

```cpp
void connection(
    PubSubClient * client
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

### variable g_loop

```cpp
EventLoop * g_loop = NULL;
```


### variable g_topic

```cpp
string g_topic;
```


### variable g_content

```cpp
string g_content;
```



## Source code

```cpp
#include "examples/hub/pubsub.h"
#include "muduo/base/ProcessInfo.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/EventLoopThread.h"

#include <iostream>
#include <stdio.h>

using namespace muduo;
using namespace muduo::net;
using namespace pubsub;

EventLoop* g_loop = NULL;
string g_topic;
string g_content;

void connection(PubSubClient* client)
{
  if (client->connected())
  {
    client->publish(g_topic, g_content);
    client->stop();
  }
  else
  {
    g_loop->quit();
  }
}

int main(int argc, char* argv[])
{
  if (argc == 4)
  {
    string hostport = argv[1];
    size_t colon = hostport.find(':');
    if (colon != string::npos)
    {
      string hostip = hostport.substr(0, colon);
      uint16_t port = static_cast<uint16_t>(atoi(hostport.c_str()+colon+1));
      g_topic = argv[2];
      g_content = argv[3];

      string name = ProcessInfo::username()+"@"+ProcessInfo::hostname();
      name += ":" + ProcessInfo::pidString();

      if (g_content == "-")
      {
        EventLoopThread loopThread;
        g_loop = loopThread.startLoop();
        PubSubClient client(g_loop, InetAddress(hostip, port), name);
        client.start();

        string line;
        while (getline(std::cin, line))
        {
          client.publish(g_topic, line);
        }
        client.stop();
        CurrentThread::sleepUsec(1000*1000);
      }
      else
      {
        EventLoop loop;
        g_loop = &loop;
        PubSubClient client(g_loop, InetAddress(hostip, port), name);
        client.setConnectionCallback(connection);
        client.start();
        loop.loop();
      }
    }
    else
    {
      printf("Usage: %s hub_ip:port topic content\n", argv[0]);
    }
  }
  else
  {
    printf("Usage: %s hub_ip:port topic content\n"
           "Read contents from stdin:\n"
           "  %s hub_ip:port topic -\n", argv[0], argv[0]);
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
