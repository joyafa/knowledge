---
title: Client

---

# Client





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[Operation](/class_client.md#enum-operation)** { kGet, kSet} |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Client](/class_client.md#function-client)**(const string & name, [EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr, [Operation](/class_client.md#enum-operation) op, int requests, int keys, int valuelen, [CountDownLatch](/classmuduo_1_1_count_down_latch.md) * connected, [CountDownLatch](/classmuduo_1_1_count_down_latch.md) * finished) |
| void | **[send](/class_client.md#function-send)**() |
| | **[Client](/class_client.md#function-client)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr, int blockSize, int sessionCount, int timeout, int threadCount) |
| const string & | **[message](/class_client.md#function-message)**() const |
| void | **[onConnect](/class_client.md#function-onconnect)**() |
| void | **[onDisconnect](/class_client.md#function-ondisconnect)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |

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

### enum Operation

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kGet | |   |
| kSet | |   |




## Public Functions Documentation

### function Client

```cpp
inline Client(
    const string & name,
    EventLoop * loop,
    const InetAddress & serverAddr,
    Operation op,
    int requests,
    int keys,
    int valuelen,
    CountDownLatch * connected,
    CountDownLatch * finished
)
```


### function send

```cpp
inline void send()
```


### function Client

```cpp
inline Client(
    EventLoop * loop,
    const InetAddress & serverAddr,
    int blockSize,
    int sessionCount,
    int timeout,
    int threadCount
)
```


### function message

```cpp
inline const string & message() const
```


### function onConnect

```cpp
inline void onConnect()
```


### function onDisconnect

```cpp
inline void onDisconnect(
    const TcpConnectionPtr & conn
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800