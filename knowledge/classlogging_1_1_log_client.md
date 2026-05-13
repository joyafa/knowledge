---
title: logging::LogClient

---

# logging::LogClient





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[LogClient](/classlogging_1_1_log_client.md#function-logclient)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr) |
| void | **[connect](/classlogging_1_1_log_client.md#function-connect)**() |
| void | **[disconnect](/classlogging_1_1_log_client.md#function-disconnect)**() |
| void | **[write](/classlogging_1_1_log_client.md#function-write)**(const [StringPiece](/classmuduo_1_1_string_piece.md) & message) |

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

### function LogClient

```cpp
inline LogClient(
    EventLoop * loop,
    const InetAddress & serverAddr
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


### function write

```cpp
inline void write(
    const StringPiece & message
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800