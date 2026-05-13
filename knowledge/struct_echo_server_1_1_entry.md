---
title: EchoServer::Entry

---

# EchoServer::Entry





Inherits from [muduo::copyable](/classmuduo_1_1copyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Entry](/struct_echo_server_1_1_entry.md#function-entry)**(const WeakTcpConnectionPtr & weakConn) |
| | **[~Entry](/struct_echo_server_1_1_entry.md#function-~entry)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| WeakTcpConnectionPtr | **[weakConn_](/struct_echo_server_1_1_entry.md#variable-weakconn-)**  |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Public Functions Documentation

### function Entry

```cpp
inline explicit Entry(
    const WeakTcpConnectionPtr & weakConn
)
```


### function ~Entry

```cpp
inline ~Entry()
```


## Public Attributes Documentation

### variable weakConn_

```cpp
WeakTcpConnectionPtr weakConn_;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800