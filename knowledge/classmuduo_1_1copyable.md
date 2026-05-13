---
title: muduo::copyable

---

# muduo::copyable



 [More...](#detailed-description)


`#include <copyable.h>`

Inherited by [muduo::Date](/classmuduo_1_1_date.md), [muduo::TimeZone](/classmuduo_1_1_time_zone.md), [muduo::Timestamp](/classmuduo_1_1_timestamp.md), [muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md), [muduo::net::HttpContext](/classmuduo_1_1net_1_1_http_context.md), [muduo::net::HttpRequest](/classmuduo_1_1net_1_1_http_request.md), [muduo::net::HttpResponse](/classmuduo_1_1net_1_1_http_response.md), [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md), [muduo::net::TimerId](/classmuduo_1_1net_1_1_timer_id.md), [pubsub::Topic](/classpubsub_1_1_topic.md)

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |

## Detailed Description

```cpp
class muduo::copyable;
```


A tag class emphasises the objects are copyable. The empty base class optimization applies. Any derived class of copyable should be a value type. 

## Protected Functions Documentation

### function copyable

```cpp
copyable() =default
```


### function ~copyable

```cpp
~copyable() =default
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800