---
title: muduo::net::ProtobufCodecLiteT

---

# muduo::net::ProtobufCodecLiteT



 [More...](#detailed-description)


`#include <ProtobufCodecLite.h>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::shared_ptr< MSG > | **[ConcreteMessagePtr](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#typedef-concretemessageptr)**  |
| typedef std::function< void(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, const [ConcreteMessagePtr](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#typedef-concretemessageptr) &, [Timestamp](/class_timestamp.md))> | **[ProtobufMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#typedef-protobufmessagecallback)**  |
| typedef [ProtobufCodecLite::RawMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#typedef-rawmessagecallback) | **[RawMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#typedef-rawmessagecallback)**  |
| typedef [ProtobufCodecLite::ErrorCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#typedef-errorcallback) | **[ErrorCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#typedef-errorcallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ProtobufCodecLiteT](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#function-protobufcodeclitet)**(const [ProtobufMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#typedef-protobufmessagecallback) & messageCb, const [RawMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#typedef-rawmessagecallback) & rawCb =[RawMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#typedef-rawmessagecallback)(), const [ErrorCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#typedef-errorcallback) & errorCb =[ProtobufCodecLite::defaultErrorCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-defaulterrorcallback)) |
| const string & | **[tag](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#function-tag)**() const |
| void | **[send](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#function-send)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, const MSG & message) |
| void | **[onMessage](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#function-onmessage)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) receiveTime) |
| void | **[onRpcMessage](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#function-onrpcmessage)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, const [MessagePtr](/namespacemuduo_1_1net.md#typedef-messageptr) & message, [Timestamp](/class_timestamp.md) receiveTime) |
| void | **[fillEmptyBuffer](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md#function-fillemptybuffer)**([muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) * buf, const MSG & message) |

## Detailed Description

```cpp
template <typename MSG ,
const char * TAG,
typename CODEC  =ProtobufCodecLite>
class muduo::net::ProtobufCodecLiteT;
```

## Public Types Documentation

### typedef ConcreteMessagePtr

```cpp
typedef std::shared_ptr<MSG> muduo::net::ProtobufCodecLiteT< MSG, TAG, CODEC >::ConcreteMessagePtr;
```


### typedef ProtobufMessageCallback

```cpp
typedef std::function<void (const TcpConnectionPtr&, const ConcreteMessagePtr&, Timestamp)> muduo::net::ProtobufCodecLiteT< MSG, TAG, CODEC >::ProtobufMessageCallback;
```


### typedef RawMessageCallback

```cpp
typedef ProtobufCodecLite::RawMessageCallback muduo::net::ProtobufCodecLiteT< MSG, TAG, CODEC >::RawMessageCallback;
```


### typedef ErrorCallback

```cpp
typedef ProtobufCodecLite::ErrorCallback muduo::net::ProtobufCodecLiteT< MSG, TAG, CODEC >::ErrorCallback;
```


## Public Functions Documentation

### function ProtobufCodecLiteT

```cpp
inline explicit ProtobufCodecLiteT(
    const ProtobufMessageCallback & messageCb,
    const RawMessageCallback & rawCb =RawMessageCallback(),
    const ErrorCallback & errorCb =ProtobufCodecLite::defaultErrorCallback
)
```


### function tag

```cpp
inline const string & tag() const
```


### function send

```cpp
inline void send(
    const TcpConnectionPtr & conn,
    const MSG & message
)
```


### function onMessage

```cpp
inline void onMessage(
    const TcpConnectionPtr & conn,
    Buffer * buf,
    Timestamp receiveTime
)
```


### function onRpcMessage

```cpp
inline void onRpcMessage(
    const TcpConnectionPtr & conn,
    const MessagePtr & message,
    Timestamp receiveTime
)
```


### function fillEmptyBuffer

```cpp
inline void fillEmptyBuffer(
    muduo::net::Buffer * buf,
    const MSG & message
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800