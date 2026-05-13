---
title: Tunnel

---

# Tunnel






`#include <tunnel.h>`

Inherits from std::enable_shared_from_this< Tunnel >, [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Tunnel](/class_tunnel.md#function-tunnel)**([muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * loop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & serverAddr, const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & serverConn) |
| | **[~Tunnel](/class_tunnel.md#function-~tunnel)**() |
| void | **[setup](/class_tunnel.md#function-setup)**() |
| void | **[connect](/class_tunnel.md#function-connect)**() |
| void | **[disconnect](/class_tunnel.md#function-disconnect)**() |

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

### function Tunnel

```cpp
inline Tunnel(
    muduo::net::EventLoop * loop,
    const muduo::net::InetAddress & serverAddr,
    const muduo::net::TcpConnectionPtr & serverConn
)
```


### function ~Tunnel

```cpp
inline ~Tunnel()
```


### function setup

```cpp
inline void setup()
```


### function connect

```cpp
inline void connect()
```


### function disconnect

```cpp
inline void disconnect()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800