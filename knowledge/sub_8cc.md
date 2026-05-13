---
title: examples/hub/sub.cc

---

# examples/hub/sub.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[subscription](/sub_8cc.md#function-subscription)**(const string & topic, const string & content, [Timestamp](/class_timestamp.md) ) |
| void | **[connection](/sub_8cc.md#function-connection)**([PubSubClient](/classpubsub_1_1_pub_sub_client.md) * client) |
| int | **[main](/sub_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [EventLoop](/class_event_loop.md) * | **[g_loop](/sub_8cc.md#variable-g-loop)**  |
| std::vector< string > | **[g_topics](/sub_8cc.md#variable-g-topics)**  |


## Functions Documentation

### function subscription

```cpp
void subscription(
    const string & topic,
    const string & content,
    Timestamp 
)
```


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


### variable g_topics

```cpp
std::vector< string > g_topics;
```



## Source code

```cpp
#include "examples/hub/pubsub.h"
#include "muduo/base/ProcessInfo.h"
#include "muduo/net/EventLoop.h"

#include <vector>
#include <stdio.h>

using namespace muduo;
using namespace muduo::net;
using namespace pubsub;

EventLoop* g_loop = NULL;
std::vector<string> g_topics;

void subscription(const string& topic, const string& content, Timestamp)
{
  printf("%s: %s\n", topic.c_str(), content.c_str());
}

void connection(PubSubClient* client)
{
  if (client->connected())
  {
    for (std::vector<string>::iterator it = g_topics.begin();
        it != g_topics.end(); ++it)
    {
      client->subscribe(*it, subscription);
    }
  }
  else
  {
    g_loop->quit();
  }
}

int main(int argc, char* argv[])
{
  if (argc > 2)
  {
    string hostport = argv[1];
    size_t colon = hostport.find(':');
    if (colon != string::npos)
    {
      string hostip = hostport.substr(0, colon);
      uint16_t port = static_cast<uint16_t>(atoi(hostport.c_str()+colon+1));
      for (int i = 2; i < argc; ++i)
      {
        g_topics.push_back(argv[i]);
      }

      EventLoop loop;
      g_loop = &loop;
      string name = ProcessInfo::username()+"@"+ProcessInfo::hostname();
      name += ":" + ProcessInfo::pidString();
      PubSubClient client(&loop, InetAddress(hostip, port), name);
      client.setConnectionCallback(connection);
      client.start();
      loop.loop();
    }
    else
    {
      printf("Usage: %s hub_ip:port topic [topic ...]\n", argv[0]);
    }
  }
  else
  {
    printf("Usage: %s hub_ip:port topic [topic ...]\n", argv[0]);
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
