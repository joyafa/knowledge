---
title: ProtobufCodec

---

# ProtobufCodec






`#include <codec.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[ErrorCode](/class_protobuf_codec.md#enum-errorcode)** { kNoError = 0, kInvalidLength, kCheckSumError, kInvalidNameLen, kUnknownMessageType, kParseError} |
| typedef std::function< void(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, const [MessagePtr](/protobuf_2codec_2codec_8h.md#typedef-messageptr) &, [muduo::Timestamp](/classmuduo_1_1_timestamp.md))> | **[ProtobufMessageCallback](/class_protobuf_codec.md#typedef-protobufmessagecallback)**  |
| typedef std::function< void(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, [muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) *, [muduo::Timestamp](/classmuduo_1_1_timestamp.md), [ErrorCode](/class_protobuf_codec.md#enum-errorcode))> | **[ErrorCallback](/class_protobuf_codec.md#typedef-errorcallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ProtobufCodec](/class_protobuf_codec.md#function-protobufcodec)**(const [ProtobufMessageCallback](/class_protobuf_codec.md#typedef-protobufmessagecallback) & messageCb) |
| | **[ProtobufCodec](/class_protobuf_codec.md#function-protobufcodec)**(const [ProtobufMessageCallback](/class_protobuf_codec.md#typedef-protobufmessagecallback) & messageCb, const [ErrorCallback](/class_protobuf_codec.md#typedef-errorcallback) & errorCb) |
| void | **[onMessage](/class_protobuf_codec.md#function-onmessage)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) * buf, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) receiveTime) |
| void | **[send](/class_protobuf_codec.md#function-send)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, const google::protobuf::Message & message) |
| const muduo::string & | **[errorCodeToString](/class_protobuf_codec.md#function-errorcodetostring)**([ErrorCode](/class_protobuf_codec.md#enum-errorcode) errorCode) |
| void | **[fillEmptyBuffer](/class_protobuf_codec.md#function-fillemptybuffer)**([muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) * buf, const google::protobuf::Message & message) |
| google::protobuf::Message * | **[createMessage](/class_protobuf_codec.md#function-createmessage)**(const std::string & type_name) |
| [MessagePtr](/protobuf_2codec_2codec_8h.md#typedef-messageptr) | **[parse](/class_protobuf_codec.md#function-parse)**(const char * buf, int len, [ErrorCode](/class_protobuf_codec.md#enum-errorcode) * errorCode) |

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

### enum ErrorCode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kNoError | 0|   |
| kInvalidLength | |   |
| kCheckSumError | |   |
| kInvalidNameLen | |   |
| kUnknownMessageType | |   |
| kParseError | |   |




### typedef ProtobufMessageCallback

```cpp
typedef std::function<void (const muduo::net::TcpConnectionPtr&, const MessagePtr&, muduo::Timestamp)> ProtobufCodec::ProtobufMessageCallback;
```


### typedef ErrorCallback

```cpp
typedef std::function<void (const muduo::net::TcpConnectionPtr&, muduo::net::Buffer*, muduo::Timestamp, ErrorCode)> ProtobufCodec::ErrorCallback;
```


## Public Functions Documentation

### function ProtobufCodec

```cpp
inline explicit ProtobufCodec(
    const ProtobufMessageCallback & messageCb
)
```


### function ProtobufCodec

```cpp
inline ProtobufCodec(
    const ProtobufMessageCallback & messageCb,
    const ErrorCallback & errorCb
)
```


### function onMessage

```cpp
void onMessage(
    const muduo::net::TcpConnectionPtr & conn,
    muduo::net::Buffer * buf,
    muduo::Timestamp receiveTime
)
```


### function send

```cpp
inline void send(
    const muduo::net::TcpConnectionPtr & conn,
    const google::protobuf::Message & message
)
```


### function errorCodeToString

```cpp
static const muduo::string & errorCodeToString(
    ErrorCode errorCode
)
```


### function fillEmptyBuffer

```cpp
static void fillEmptyBuffer(
    muduo::net::Buffer * buf,
    const google::protobuf::Message & message
)
```


'ByteSize()' of message is deprecated in Protocol Buffers v3.4.0 firstly. But, till to v3.11.0, it just getting start to be marked by '**attribute**((deprecated()))'. So, here, v3.9.2 is selected as maximum version using 'ByteSize()' to avoid potential effect for previous muduo code/projects as far as possible. Note: All information above just INFER from 1) [https://github.com/protocolbuffers/protobuf/releases/tag/v3.4.0](https://github.com/protocolbuffers/protobuf/releases/tag/v3.4.0) 2) MACRO in file 'include/google/protobuf/port_def.inc'. eg. '#define PROTOBUF_DEPRECATED_MSG(msg) **attribute**((deprecated(msg)))'. In addition, usage of 'ToIntSize()' comes from Impl of ByteSize() in new version's Protocol Buffers.


### function createMessage

```cpp
static google::protobuf::Message * createMessage(
    const std::string & type_name
)
```


### function parse

```cpp
static MessagePtr parse(
    const char * buf,
    int len,
    ErrorCode * errorCode
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800