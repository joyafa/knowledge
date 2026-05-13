---
title: examples/curl/mcurl.cc

---

# examples/curl/mcurl.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[onData](/mcurl_8cc.md#function-ondata)**(const char * data, int len) |
| void | **[done](/mcurl_8cc.md#function-done)**([curl::Request](/classcurl_1_1_request.md) * c, int code) |
| void | **[done2](/mcurl_8cc.md#function-done2)**([curl::Request](/classcurl_1_1_request.md) * c, int code) |
| int | **[main](/mcurl_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [EventLoop](/class_event_loop.md) * | **[g_loop](/mcurl_8cc.md#variable-g-loop)**  |


## Functions Documentation

### function onData

```cpp
void onData(
    const char * data,
    int len
)
```


### function done

```cpp
void done(
    curl::Request * c,
    int code
)
```


### function done2

```cpp
void done2(
    curl::Request * c,
    int code
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



## Source code

```cpp
#include "examples/curl/Curl.h"
#include "muduo/net/EventLoop.h"
#include <stdio.h>

using namespace muduo::net;

EventLoop* g_loop = NULL;

void onData(const char* data, int len)
{
  printf("len %d\n", len);
}

void done(curl::Request* c, int code)
{
  printf("done %p %s %d\n", c, c->getEffectiveUrl(), code);
}

void done2(curl::Request* c, int code)
{
  printf("done2 %p %s %d %d\n", c, c->getRedirectUrl(), c->getResponseCode(), code);
  // g_loop->quit();
}

int main(int argc, char* argv[])
{
  EventLoop loop;
  g_loop = &loop;
  loop.runAfter(30.0, std::bind(&EventLoop::quit, &loop));
  curl::Curl::initialize(curl::Curl::kCURLssl);
  curl::Curl curl(&loop);

  curl::RequestPtr req = curl.getUrl("http://chenshuo.com");
  req->setDataCallback(onData);
  req->setDoneCallback(done);

  curl::RequestPtr req2 = curl.getUrl("https://github.com");
  // req2->allowRedirect(5);
  req2->setDataCallback(onData);
  req2->setDoneCallback(done);

  curl::RequestPtr req3 = curl.getUrl("http://example.com");
  // req3->allowRedirect(5);
  req3->setDataCallback(onData);
  req3->setDoneCallback(done2);

  loop.loop();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
