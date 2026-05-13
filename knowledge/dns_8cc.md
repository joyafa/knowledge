---
title: examples/cdns/dns.cc

---

# examples/cdns/dns.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[quit](/dns_8cc.md#function-quit)**() |
| void | **[resolveCallback](/dns_8cc.md#function-resolvecallback)**(const string & host, const [InetAddress](/class_inet_address.md) & addr) |
| void | **[resolve](/dns_8cc.md#function-resolve)**([Resolver](/classcdns_1_1_resolver.md) * res, const string & host) |
| int | **[main](/dns_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [EventLoop](/class_event_loop.md) * | **[g_loop](/dns_8cc.md#variable-g-loop)**  |
| int | **[count](/dns_8cc.md#variable-count)**  |
| int | **[total](/dns_8cc.md#variable-total)**  |


## Functions Documentation

### function quit

```cpp
void quit()
```


### function resolveCallback

```cpp
void resolveCallback(
    const string & host,
    const InetAddress & addr
)
```


### function resolve

```cpp
void resolve(
    Resolver * res,
    const string & host
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
EventLoop * g_loop;
```


### variable count

```cpp
int count = 0;
```


### variable total

```cpp
int total = 0;
```



## Source code

```cpp
#include "examples/cdns/Resolver.h"
#include "muduo/net/EventLoop.h"
#include <stdio.h>

using namespace muduo;
using namespace muduo::net;
using namespace cdns;

EventLoop* g_loop;
int count = 0;
int total = 0;

void quit()
{
  g_loop->quit();
}

void resolveCallback(const string& host, const InetAddress& addr)
{
  printf("resolveCallback %s -> %s\n", host.c_str(), addr.toIpPort().c_str());
  if (++count == total)
    quit();
}

void resolve(Resolver* res, const string& host)
{
  res->resolve(host, std::bind(&resolveCallback, host, _1));
}

int main(int argc, char* argv[])
{
  EventLoop loop;
  loop.runAfter(10, quit);
  g_loop = &loop;
  Resolver resolver(&loop,
                   argc == 1 ? Resolver::kDNSonly : Resolver::kDNSandHostsFile);
  if (argc == 1)
  {
    total = 3;
    resolve(&resolver, "www.chenshuo.com");
    resolve(&resolver, "www.example.com");
    resolve(&resolver, "www.google.com");
  }
  else
  {
    total = argc-1;
    for (int i = 1; i < argc; ++i)
      resolve(&resolver, argv[i]);
  }
  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
