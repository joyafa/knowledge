---
title: pubsub::Topic

---

# pubsub::Topic





Inherits from [muduo::copyable](/classmuduo_1_1copyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Topic](/classpubsub_1_1_topic.md#function-topic)**(const string & topic) |
| void | **[add](/classpubsub_1_1_topic.md#function-add)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[remove](/classpubsub_1_1_topic.md#function-remove)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[publish](/classpubsub_1_1_topic.md#function-publish)**(const string & content, [Timestamp](/class_timestamp.md) time) |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Public Functions Documentation

### function Topic

```cpp
inline Topic(
    const string & topic
)
```


### function add

```cpp
inline void add(
    const TcpConnectionPtr & conn
)
```


### function remove

```cpp
inline void remove(
    const TcpConnectionPtr & conn
)
```


### function publish

```cpp
inline void publish(
    const string & content,
    Timestamp time
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800