---
title: ChatClient

---

# ChatClient





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ChatClient](/class_chat_client.md#function-chatclient)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr) |
| void | **[connect](/class_chat_client.md#function-connect)**() |
| void | **[disconnect](/class_chat_client.md#function-disconnect)**() |
| void | **[write](/class_chat_client.md#function-write)**(const [StringPiece](/classmuduo_1_1_string_piece.md) & message) |
| | **[ChatClient](/class_chat_client.md#function-chatclient)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr) |
| void | **[connect](/class_chat_client.md#function-connect)**() |
| void | **[disconnect](/class_chat_client.md#function-disconnect)**() |
| [Timestamp](/class_timestamp.md) | **[receiveTime](/class_chat_client.md#function-receivetime)**() const |

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


## Public Functions Documentation

### function ChatClient

```cpp
inline ChatClient(
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


### function ChatClient

```cpp
inline ChatClient(
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


### function receiveTime

```cpp
inline Timestamp receiveTime() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800