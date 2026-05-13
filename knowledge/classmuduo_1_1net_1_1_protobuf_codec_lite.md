---
title: muduo::net::ProtobufCodecLite

---

# muduo::net::ProtobufCodecLite






`#include <ProtobufCodecLite.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[ErrorCode](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#enum-errorcode)** { kNoError = 0, kInvalidLength, kCheckSumError, kInvalidNameLen, kUnknownMessageType, kParseError} |
| typedef std::function< bool(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, [StringPiece](/classmuduo_1_1_string_piece.md), [Timestamp](/class_timestamp.md))> | **[RawMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#typedef-rawmessagecallback)**  |
| typedef std::function< void(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, const [MessagePtr](/namespacemuduo_1_1net.md#typedef-messageptr) &, [Timestamp](/class_timestamp.md))> | **[ProtobufMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#typedef-protobufmessagecallback)**  |
| typedef std::function< void(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, [Buffer](/class_buffer.md) *, [Timestamp](/class_timestamp.md), [ErrorCode](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#enum-errorcode))> | **[ErrorCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#typedef-errorcallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ProtobufCodecLite](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-protobufcodeclite)**(const ::google::protobuf::Message * prototype, [StringPiece](/classmuduo_1_1_string_piece.md) tagArg, const [ProtobufMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#typedef-protobufmessagecallback) & messageCb, const [RawMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#typedef-rawmessagecallback) & rawCb =[RawMessageCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#typedef-rawmessagecallback)(), const [ErrorCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#typedef-errorcallback) & errorCb =[defaultErrorCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-defaulterrorcallback)) =default |
| virtual | **[~ProtobufCodecLite](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-~protobufcodeclite)**() =default |
| const string & | **[tag](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-tag)**() const |
| void | **[send](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-send)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, const ::google::protobuf::Message & message) |
| void | **[onMessage](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-onmessage)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) receiveTime) |
| virtual bool | **[parseFromBuffer](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-parsefrombuffer)**([StringPiece](/classmuduo_1_1_string_piece.md) buf, google::protobuf::Message * message) |
| virtual int | **[serializeToBuffer](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-serializetobuffer)**(const google::protobuf::Message & message, [Buffer](/class_buffer.md) * buf) |
| [ErrorCode](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#enum-errorcode) | **[parse](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-parse)**(const char * buf, int len, ::google::protobuf::Message * message) |
| void | **[fillEmptyBuffer](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-fillemptybuffer)**([muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md) * buf, const google::protobuf::Message & message) |
| const string & | **[errorCodeToString](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-errorcodetostring)**([ErrorCode](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#enum-errorcode) errorCode) |
| int32_t | **[checksum](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-checksum)**(const void * buf, int len) |
| bool | **[validateChecksum](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-validatechecksum)**(const char * buf, int len) |
| int32_t | **[asInt32](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-asint32)**(const char * buf) |
| void | **[defaultErrorCallback](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#function-defaulterrorcallback)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) , [ErrorCode](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#enum-errorcode) errorCode) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const int | **[kHeaderLen](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#variable-kheaderlen)**  |
| const int | **[kChecksumLen](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#variable-kchecksumlen)**  |
| const int | **[kMaxMessageLen](/classmuduo_1_1net_1_1_protobuf_codec_lite.md#variable-kmaxmessagelen)**  |

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




### typedef RawMessageCallback

```cpp
typedef std::function<bool (const TcpConnectionPtr&, StringPiece, Timestamp)> muduo::net::ProtobufCodecLite::RawMessageCallback;
```


### typedef ProtobufMessageCallback

```cpp
typedef std::function<void (const TcpConnectionPtr&, const MessagePtr&, Timestamp)> muduo::net::ProtobufCodecLite::ProtobufMessageCallback;
```


### typedef ErrorCallback

```cpp
typedef std::function<void (const TcpConnectionPtr&, Buffer*, Timestamp, ErrorCode)> muduo::net::ProtobufCodecLite::ErrorCallback;
```


## Public Functions Documentation

### function ProtobufCodecLite

```cpp
inline ProtobufCodecLite(
    const ::google::protobuf::Message * prototype,
    StringPiece tagArg,
    const ProtobufMessageCallback & messageCb,
    const RawMessageCallback & rawCb =RawMessageCallback(),
    const ErrorCallback & errorCb =defaultErrorCallback
) =default
```


### function ~ProtobufCodecLite

```cpp
virtual ~ProtobufCodecLite() =default
```


### function tag

```cpp
inline const string & tag() const
```


### function send

```cpp
void send(
    const TcpConnectionPtr & conn,
    const ::google::protobuf::Message & message
)
```


### function onMessage

```cpp
void onMessage(
    const TcpConnectionPtr & conn,
    Buffer * buf,
    Timestamp receiveTime
)
```


### function parseFromBuffer

```cpp
virtual bool parseFromBuffer(
    StringPiece buf,
    google::protobuf::Message * message
)
```


### function serializeToBuffer

```cpp
virtual int serializeToBuffer(
    const google::protobuf::Message & message,
    Buffer * buf
)
```


'ByteSize()' of message is deprecated in Protocol Buffers v3.4.0 firstly. But, till to v3.11.0, it just getting start to be marked by '**attribute**((deprecated()))'. So, here, v3.9.2 is selected as maximum version using 'ByteSize()' to avoid potential effect for previous muduo code/projects as far as possible. Note: All information above just INFER from 1) [https://github.com/protocolbuffers/protobuf/releases/tag/v3.4.0](https://github.com/protocolbuffers/protobuf/releases/tag/v3.4.0) 2) MACRO in file 'include/google/protobuf/port_def.inc'. eg. '#define PROTOBUF_DEPRECATED_MSG(msg) **attribute**((deprecated(msg)))'. In addition, usage of 'ToIntSize()' comes from Impl of ByteSize() in new version's Protocol Buffers.


### function parse

```cpp
ErrorCode parse(
    const char * buf,
    int len,
    ::google::protobuf::Message * message
)
```


### function fillEmptyBuffer

```cpp
void fillEmptyBuffer(
    muduo::net::Buffer * buf,
    const google::protobuf::Message & message
)
```


### function errorCodeToString

```cpp
static const string & errorCodeToString(
    ErrorCode errorCode
)
```


### function checksum

```cpp
static int32_t checksum(
    const void * buf,
    int len
)
```


### function validateChecksum

```cpp
static bool validateChecksum(
    const char * buf,
    int len
)
```


### function asInt32

```cpp
static int32_t asInt32(
    const char * buf
)
```


### function defaultErrorCallback

```cpp
static void defaultErrorCallback(
    const TcpConnectionPtr & conn,
    Buffer * buf,
    Timestamp ,
    ErrorCode errorCode
)
```


## Public Attributes Documentation

### variable kHeaderLen

```cpp
static const int kHeaderLen = sizeof(int32_t);
```


### variable kChecksumLen

```cpp
static const int kChecksumLen = sizeof(int32_t);
```


### variable kMaxMessageLen

```cpp
static const int kMaxMessageLen = 64*1024*1024;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800