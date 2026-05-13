---
title: BackendSession

---

# BackendSession





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BackendSession](/class_backend_session.md#function-backendsession)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & backendAddr, const string & name) |
| void | **[connect](/class_backend_session.md#function-connect)**() |
| bool | **[send](/class_backend_session.md#function-send)**(RpcMessage & msg, const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & clientConn) |
| | **[BackendSession](/class_backend_session.md#function-backendsession)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & backendAddr, const string & name) |
| void | **[connect](/class_backend_session.md#function-connect)**() |
| template <typename MSG \> <br>bool | **[send](/class_backend_session.md#function-send)**(MSG & msg, const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & clientConn) |

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

### function BackendSession

```cpp
inline BackendSession(
    EventLoop * loop,
    const InetAddress & backendAddr,
    const string & name
)
```


### function connect

```cpp
inline void connect()
```


### function send

```cpp
inline bool send(
    RpcMessage & msg,
    const TcpConnectionPtr & clientConn
)
```


### function BackendSession

```cpp
inline BackendSession(
    EventLoop * loop,
    const InetAddress & backendAddr,
    const string & name
)
```


### function connect

```cpp
inline void connect()
```


### function send

```cpp
template <typename MSG >
inline bool send(
    MSG & msg,
    const TcpConnectionPtr & clientConn
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800