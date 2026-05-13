---
title: pubsub::PubSubServer

---

# pubsub::PubSubServer





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[PubSubServer](/classpubsub_1_1_pub_sub_server.md#function-pubsubserver)**([muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * loop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & listenAddr) |
| void | **[start](/classpubsub_1_1_pub_sub_server.md#function-start)**() |

## Additional inherited members

**Public Functions inherited from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**(const noncopyable & ) =delete |
| void | **[operator=](/classmuduo_1_1noncopyable.md#function-operator=)**(const [noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable) & ) =delete |

**Protected Functions inherited from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**() =default |
| | **[~noncopyable](/classmuduo_1_1noncopyable.md#function-~noncopyable)**() =default |


## Public Functions Documentation

### function PubSubServer

```cpp
inline PubSubServer(
    muduo::net::EventLoop * loop,
    const muduo::net::InetAddress & listenAddr
)
```


### function start

```cpp
inline void start()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800