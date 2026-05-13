---
title: CallbackT

---

# CallbackT



 [More...](#detailed-description)


`#include <dispatcher.h>`

Inherits from [Callback](/class_callback.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, const std::shared_ptr< T > &message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md))> | **[ProtobufMessageTCallback](/class_callback_t.md#typedef-protobufmessagetcallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[CallbackT](/class_callback_t.md#function-callbackt)**(const [ProtobufMessageTCallback](/class_callback_t.md#typedef-protobufmessagetcallback) & callback) |
| virtual void | **[onMessage](/class_callback_t.md#function-onmessage)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, const [MessagePtr](/dispatcher_8h.md#typedef-messageptr) & message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) receiveTime) const override |

## Additional inherited members

**Public Functions inherited from [Callback](/class_callback.md)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~Callback](/class_callback.md#function-~callback)**() =default |

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


## Detailed Description

```cpp
template <typename T >
class CallbackT;
```

## Public Types Documentation

### typedef ProtobufMessageTCallback

```cpp
typedef std::function<void (const muduo::net::TcpConnectionPtr&, const std::shared_ptr<T>& message, muduo::Timestamp)> CallbackT< T >::ProtobufMessageTCallback;
```


## Public Functions Documentation

### function CallbackT

```cpp
inline CallbackT(
    const ProtobufMessageTCallback & callback
)
```


### function onMessage

```cpp
inline virtual void onMessage(
    const muduo::net::TcpConnectionPtr & conn,
    const MessagePtr & message,
    muduo::Timestamp receiveTime
) const override
```


**Reimplements**: [Callback::onMessage](/class_callback.md#function-onmessage)


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800