---
title: RpcClient

---

# RpcClient





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[RpcClient](/class_rpc_client.md#function-rpcclient)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr) |
| void | **[connect](/class_rpc_client.md#function-connect)**() |
| | **[RpcClient](/class_rpc_client.md#function-rpcclient)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr) |
| void | **[connect](/class_rpc_client.md#function-connect)**() |
| | **[RpcClient](/class_rpc_client.md#function-rpcclient)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr, [CountDownLatch](/classmuduo_1_1_count_down_latch.md) * allConnected, [CountDownLatch](/classmuduo_1_1_count_down_latch.md) * allFinished) |
| void | **[connect](/class_rpc_client.md#function-connect)**() |
| void | **[sendRequest](/class_rpc_client.md#function-sendrequest)**() |

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

### function RpcClient

```cpp
inline RpcClient(
    EventLoop * loop,
    const InetAddress & serverAddr
)
```


### function connect

```cpp
inline void connect()
```


### function RpcClient

```cpp
inline RpcClient(
    EventLoop * loop,
    const InetAddress & serverAddr
)
```


### function connect

```cpp
inline void connect()
```


### function RpcClient

```cpp
inline RpcClient(
    EventLoop * loop,
    const InetAddress & serverAddr,
    CountDownLatch * allConnected,
    CountDownLatch * allFinished
)
```


### function connect

```cpp
inline void connect()
```


### function sendRequest

```cpp
inline void sendRequest()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800