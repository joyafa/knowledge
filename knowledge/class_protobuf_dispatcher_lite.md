---
title: ProtobufDispatcherLite

---

# ProtobufDispatcherLite






`#include <dispatcher_lite.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, const [MessagePtr](/dispatcher__lite_8h.md#typedef-messageptr) &, [muduo::Timestamp](/classmuduo_1_1_timestamp.md))> | **[ProtobufMessageCallback](/class_protobuf_dispatcher_lite.md#typedef-protobufmessagecallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ProtobufDispatcherLite](/class_protobuf_dispatcher_lite.md#function-protobufdispatcherlite)**(const [ProtobufMessageCallback](/class_protobuf_dispatcher_lite.md#typedef-protobufmessagecallback) & defaultCb) |
| void | **[onProtobufMessage](/class_protobuf_dispatcher_lite.md#function-onprotobufmessage)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, const [MessagePtr](/dispatcher__lite_8h.md#typedef-messageptr) & message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) receiveTime) const |
| void | **[registerMessageCallback](/class_protobuf_dispatcher_lite.md#function-registermessagecallback)**(const google::protobuf::Descriptor * desc, const [ProtobufMessageCallback](/class_protobuf_dispatcher_lite.md#typedef-protobufmessagecallback) & callback) |

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

### typedef ProtobufMessageCallback

```cpp
typedef std::function<void (const muduo::net::TcpConnectionPtr&, const MessagePtr&, muduo::Timestamp)> ProtobufDispatcherLite::ProtobufMessageCallback;
```


## Public Functions Documentation

### function ProtobufDispatcherLite

```cpp
inline explicit ProtobufDispatcherLite(
    const ProtobufMessageCallback & defaultCb
)
```


### function onProtobufMessage

```cpp
inline void onProtobufMessage(
    const muduo::net::TcpConnectionPtr & conn,
    const MessagePtr & message,
    muduo::Timestamp receiveTime
) const
```


### function registerMessageCallback

```cpp
inline void registerMessageCallback(
    const google::protobuf::Descriptor * desc,
    const ProtobufMessageCallback & callback
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800