---
title: LengthHeaderCodec

---

# LengthHeaderCodec






`#include <codec.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, const muduo::string &message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md))> | **[StringMessageCallback](/class_length_header_codec.md#typedef-stringmessagecallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[LengthHeaderCodec](/class_length_header_codec.md#function-lengthheadercodec)**(const [StringMessageCallback](/class_length_header_codec.md#typedef-stringmessagecallback) & cb) |
| void | **[onMessage](/class_length_header_codec.md#function-onmessage)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) * buf, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) receiveTime) |
| void | **[send](/class_length_header_codec.md#function-send)**([muduo::net::TcpConnection](/classmuduo_1_1net_1_1_tcp_connection.md) * conn, const [muduo::StringPiece](/classmuduo_1_1_string_piece.md) & message) |

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

### typedef StringMessageCallback

```cpp
typedef std::function<void (const muduo::net::TcpConnectionPtr&, const muduo::string& message, muduo::Timestamp)> LengthHeaderCodec::StringMessageCallback;
```


## Public Functions Documentation

### function LengthHeaderCodec

```cpp
inline explicit LengthHeaderCodec(
    const StringMessageCallback & cb
)
```


### function onMessage

```cpp
inline void onMessage(
    const muduo::net::TcpConnectionPtr & conn,
    muduo::net::Buffer * buf,
    muduo::Timestamp receiveTime
)
```


### function send

```cpp
inline void send(
    muduo::net::TcpConnection * conn,
    const muduo::StringPiece & message
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800