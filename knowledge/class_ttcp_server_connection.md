---
title: TtcpServerConnection

---

# TtcpServerConnection





Inherits from std::enable_shared_from_this< TtcpServerConnection >, [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[TtcpServerConnection](/class_ttcp_server_connection.md#function-ttcpserverconnection)**(boost::asio::io_service & io_service) |
| | **[~TtcpServerConnection](/class_ttcp_server_connection.md#function-~ttcpserverconnection)**() |
| tcp::socket & | **[socket](/class_ttcp_server_connection.md#function-socket)**() |
| void | **[start](/class_ttcp_server_connection.md#function-start)**() |

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

### function TtcpServerConnection

```cpp
inline TtcpServerConnection(
    boost::asio::io_service & io_service
)
```


### function ~TtcpServerConnection

```cpp
inline ~TtcpServerConnection()
```


### function socket

```cpp
inline tcp::socket & socket()
```


### function start

```cpp
inline void start()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800