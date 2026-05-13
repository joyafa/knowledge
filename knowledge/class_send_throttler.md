---
title: SendThrottler

---

# SendThrottler





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SendThrottler](/class_send_throttler.md#function-sendthrottler)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & addr) |
| void | **[connect](/class_send_throttler.md#function-connect)**() |
| void | **[disconnect](/class_send_throttler.md#function-disconnect)**() |
| void | **[send](/class_send_throttler.md#function-send)**(const string & word, int64_t count) |

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

### function SendThrottler

```cpp
inline SendThrottler(
    EventLoop * loop,
    const InetAddress & addr
)
```


### function connect

```cpp
inline void connect()
```


### function disconnect

```cpp
inline void disconnect()
```


### function send

```cpp
inline void send(
    const string & word,
    int64_t count
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800