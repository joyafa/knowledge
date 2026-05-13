---
title: pubsub::PubSubClient

---

# pubsub::PubSubClient






`#include <pubsub.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void([PubSubClient](/classpubsub_1_1_pub_sub_client.md#function-pubsubclient) *)> | **[ConnectionCallback](/classpubsub_1_1_pub_sub_client.md#typedef-connectioncallback)**  |
| typedef std::function< void(const string &topic, const string &content, [muduo::Timestamp](/classmuduo_1_1_timestamp.md))> | **[SubscribeCallback](/classpubsub_1_1_pub_sub_client.md#typedef-subscribecallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[PubSubClient](/classpubsub_1_1_pub_sub_client.md#function-pubsubclient)**([muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * loop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & hubAddr, const string & name) |
| void | **[start](/classpubsub_1_1_pub_sub_client.md#function-start)**() |
| void | **[stop](/classpubsub_1_1_pub_sub_client.md#function-stop)**() |
| bool | **[connected](/classpubsub_1_1_pub_sub_client.md#function-connected)**() const |
| void | **[setConnectionCallback](/classpubsub_1_1_pub_sub_client.md#function-setconnectioncallback)**(const [ConnectionCallback](/classpubsub_1_1_pub_sub_client.md#typedef-connectioncallback) & cb) |
| bool | **[subscribe](/classpubsub_1_1_pub_sub_client.md#function-subscribe)**(const string & topic, const [SubscribeCallback](/classpubsub_1_1_pub_sub_client.md#typedef-subscribecallback) & cb) |
| void | **[unsubscribe](/classpubsub_1_1_pub_sub_client.md#function-unsubscribe)**(const string & topic) |
| bool | **[publish](/classpubsub_1_1_pub_sub_client.md#function-publish)**(const string & topic, const string & content) |

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


## Public Types Documentation

### typedef ConnectionCallback

```cpp
typedef std::function<void (PubSubClient*)> pubsub::PubSubClient::ConnectionCallback;
```


### typedef SubscribeCallback

```cpp
typedef std::function<void (const string& topic, const string& content, muduo::Timestamp)> pubsub::PubSubClient::SubscribeCallback;
```


## Public Functions Documentation

### function PubSubClient

```cpp
PubSubClient(
    muduo::net::EventLoop * loop,
    const muduo::net::InetAddress & hubAddr,
    const string & name
)
```


### function start

```cpp
void start()
```


### function stop

```cpp
void stop()
```


### function connected

```cpp
bool connected() const
```


### function setConnectionCallback

```cpp
inline void setConnectionCallback(
    const ConnectionCallback & cb
)
```


### function subscribe

```cpp
bool subscribe(
    const string & topic,
    const SubscribeCallback & cb
)
```


### function unsubscribe

```cpp
void unsubscribe(
    const string & topic
)
```


### function publish

```cpp
bool publish(
    const string & topic,
    const string & content
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800