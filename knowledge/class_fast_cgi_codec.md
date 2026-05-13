---
title: FastCgiCodec

---

# FastCgiCodec






`#include <fastcgi.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[RecordHeader](/struct_fast_cgi_codec_1_1_record_header.md)**  |

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::map< std::string, std::string > | **[ParamMap](/class_fast_cgi_codec.md#typedef-parammap)**  |
| typedef std::function< void(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &conn, [ParamMap](/class_fast_cgi_codec.md#typedef-parammap) &, [muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) *)> | **[Callback](/class_fast_cgi_codec.md#typedef-callback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[FastCgiCodec](/class_fast_cgi_codec.md#function-fastcgicodec)**(const [Callback](/class_fast_cgi_codec.md#typedef-callback) & cb) |
| void | **[onMessage](/class_fast_cgi_codec.md#function-onmessage)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) * buf, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) receiveTime) |
| void | **[respond](/class_fast_cgi_codec.md#function-respond)**([muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) * response) |

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

### typedef ParamMap

```cpp
typedef std::map<std::string, std::string> FastCgiCodec::ParamMap;
```


### typedef Callback

```cpp
typedef std::function<void (const muduo::net::TcpConnectionPtr& conn, ParamMap&, muduo::net::Buffer*)> FastCgiCodec::Callback;
```


## Public Functions Documentation

### function FastCgiCodec

```cpp
inline explicit FastCgiCodec(
    const Callback & cb
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


### function respond

```cpp
static void respond(
    muduo::net::Buffer * response
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800