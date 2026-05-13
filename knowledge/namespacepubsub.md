---
title: pubsub

---

# pubsub



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[pubsub::PubSubClient](/classpubsub_1_1_pub_sub_client.md)**  |
| class | **[pubsub::PubSubServer](/classpubsub_1_1_pub_sub_server.md)**  |
| class | **[pubsub::Topic](/classpubsub_1_1_topic.md)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| enum| **[ParseResult](/namespacepubsub.md#enum-parseresult)** { kError, kSuccess, kContinue} |
| typedef std::set< string > | **[ConnectionSubscription](/namespacepubsub.md#typedef-connectionsubscription)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| [ParseResult](/namespacepubsub.md#enum-parseresult) | **[parseMessage](/namespacepubsub.md#function-parsemessage)**([muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) * buf, string * cmd, string * topic, string * content) |

## Types Documentation

### enum ParseResult

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kError | |   |
| kSuccess | |   |
| kContinue | |   |




### typedef ConnectionSubscription

```cpp
typedef std::set<string> pubsub::ConnectionSubscription;
```



## Functions Documentation

### function parseMessage

```cpp
ParseResult parseMessage(
    muduo::net::Buffer * buf,
    string * cmd,
    string * topic,
    string * content
)
```






-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800