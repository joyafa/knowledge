---
title: hiredis::Hiredis

---

# hiredis::Hiredis






`#include <Hiredis.h>`

Inherits from std::enable_shared_from_this< Hiredis >, [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void([Hiredis](/classhiredis_1_1_hiredis.md#function-hiredis) *, int)> | **[ConnectCallback](/classhiredis_1_1_hiredis.md#typedef-connectcallback)**  |
| typedef std::function< void([Hiredis](/classhiredis_1_1_hiredis.md#function-hiredis) *, int)> | **[DisconnectCallback](/classhiredis_1_1_hiredis.md#typedef-disconnectcallback)**  |
| typedef std::function< void([Hiredis](/classhiredis_1_1_hiredis.md#function-hiredis) *, redisReply *)> | **[CommandCallback](/classhiredis_1_1_hiredis.md#typedef-commandcallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Hiredis](/classhiredis_1_1_hiredis.md#function-hiredis)**([muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * loop, const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & serverAddr) |
| | **[~Hiredis](/classhiredis_1_1_hiredis.md#function-~hiredis)**() |
| const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) & | **[serverAddress](/classhiredis_1_1_hiredis.md#function-serveraddress)**() const |
| bool | **[connected](/classhiredis_1_1_hiredis.md#function-connected)**() const |
| const char * | **[errstr](/classhiredis_1_1_hiredis.md#function-errstr)**() const |
| void | **[setConnectCallback](/classhiredis_1_1_hiredis.md#function-setconnectcallback)**(const [ConnectCallback](/classhiredis_1_1_hiredis.md#typedef-connectcallback) & cb) |
| void | **[setDisconnectCallback](/classhiredis_1_1_hiredis.md#function-setdisconnectcallback)**(const [DisconnectCallback](/classhiredis_1_1_hiredis.md#typedef-disconnectcallback) & cb) |
| void | **[connect](/classhiredis_1_1_hiredis.md#function-connect)**() |
| void | **[disconnect](/classhiredis_1_1_hiredis.md#function-disconnect)**() |
| int | **[command](/classhiredis_1_1_hiredis.md#function-command)**(const [CommandCallback](/classhiredis_1_1_hiredis.md#typedef-commandcallback) & cb, [muduo::StringArg](/classmuduo_1_1_string_arg.md) cmd, ... ) |
| int | **[ping](/classhiredis_1_1_hiredis.md#function-ping)**() |

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

### typedef ConnectCallback

```cpp
typedef std::function<void(Hiredis*, int)> hiredis::Hiredis::ConnectCallback;
```


### typedef DisconnectCallback

```cpp
typedef std::function<void(Hiredis*, int)> hiredis::Hiredis::DisconnectCallback;
```


### typedef CommandCallback

```cpp
typedef std::function<void(Hiredis*, redisReply*)> hiredis::Hiredis::CommandCallback;
```


## Public Functions Documentation

### function Hiredis

```cpp
Hiredis(
    muduo::net::EventLoop * loop,
    const muduo::net::InetAddress & serverAddr
)
```


### function ~Hiredis

```cpp
~Hiredis()
```


### function serverAddress

```cpp
inline const muduo::net::InetAddress & serverAddress() const
```


### function connected

```cpp
bool connected() const
```


### function errstr

```cpp
const char * errstr() const
```


### function setConnectCallback

```cpp
inline void setConnectCallback(
    const ConnectCallback & cb
)
```


### function setDisconnectCallback

```cpp
inline void setDisconnectCallback(
    const DisconnectCallback & cb
)
```


### function connect

```cpp
void connect()
```


### function disconnect

```cpp
void disconnect()
```


### function command

```cpp
int command(
    const CommandCallback & cb,
    muduo::StringArg cmd,
    ... 
)
```


### function ping

```cpp
int ping()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800