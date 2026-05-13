---
title: Callback

---

# Callback






`#include <dispatcher.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

Inherited by [CallbackT< T >](/class_callback_t.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~Callback](/class_callback.md#function-~callback)**() =default |
| virtual void | **[onMessage](/class_callback.md#function-onmessage)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & , const [MessagePtr](/dispatcher_8h.md#typedef-messageptr) & message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) ) const =0 |

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

### function ~Callback

```cpp
virtual ~Callback() =default
```


### function onMessage

```cpp
virtual void onMessage(
    const muduo::net::TcpConnectionPtr & ,
    const MessagePtr & message,
    muduo::Timestamp 
) const =0
```


**Reimplemented by**: [CallbackT::onMessage](/class_callback_t.md#function-onmessage)


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800