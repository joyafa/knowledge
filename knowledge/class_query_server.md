---
title: QueryServer

---

# QueryServer





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[QueryServer](/class_query_server.md#function-queryserver)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr) |
| void | **[start](/class_query_server.md#function-start)**() |

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

### function QueryServer

```cpp
inline QueryServer(
    EventLoop * loop,
    const InetAddress & listenAddr
)
```


### function start

```cpp
inline void start()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800