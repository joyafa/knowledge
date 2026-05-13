---
title: ProtobufDispatcher

---

# ProtobufDispatcher






`#include <dispatcher.h>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, const [MessagePtr](/dispatcher_8h.md#typedef-messageptr) &message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md))> | **[ProtobufMessageCallback](/class_protobuf_dispatcher.md#typedef-protobufmessagecallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ProtobufDispatcher](/class_protobuf_dispatcher.md#function-protobufdispatcher)**(const [ProtobufMessageCallback](/class_protobuf_dispatcher.md#typedef-protobufmessagecallback) & defaultCb) |
| void | **[onProtobufMessage](/class_protobuf_dispatcher.md#function-onprotobufmessage)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, const [MessagePtr](/dispatcher_8h.md#typedef-messageptr) & message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) receiveTime) const |
| template <typename T \> <br>void | **[registerMessageCallback](/class_protobuf_dispatcher.md#function-registermessagecallback)**(const typename [CallbackT](/class_callback_t.md)< T >::ProtobufMessageTCallback & callback) |

## Public Types Documentation

### typedef ProtobufMessageCallback

```cpp
typedef std::function<void (const muduo::net::TcpConnectionPtr&, const MessagePtr& message, muduo::Timestamp)> ProtobufDispatcher::ProtobufMessageCallback;
```


## Public Functions Documentation

### function ProtobufDispatcher

```cpp
inline explicit ProtobufDispatcher(
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
template <typename T >
inline void registerMessageCallback(
    const typename CallbackT< T >::ProtobufMessageTCallback & callback
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800