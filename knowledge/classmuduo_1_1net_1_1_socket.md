---
title: muduo::net::Socket

---

# muduo::net::Socket



 [More...](#detailed-description)


`#include <Socket.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Socket](/classmuduo_1_1net_1_1_socket.md#function-socket)**(int sockfd) |
| | **[~Socket](/classmuduo_1_1net_1_1_socket.md#function-~socket)**() |
| int | **[fd](/classmuduo_1_1net_1_1_socket.md#function-fd)**() const |
| bool | **[getTcpInfo](/classmuduo_1_1net_1_1_socket.md#function-gettcpinfo)**(struct tcp_info * tcpi) const |
| bool | **[getTcpInfoString](/classmuduo_1_1net_1_1_socket.md#function-gettcpinfostring)**(char * buf, int len) const |
| void | **[bindAddress](/classmuduo_1_1net_1_1_socket.md#function-bindaddress)**(const [InetAddress](/class_inet_address.md) & localaddr)<br>abort if address in use  |
| void | **[listen](/classmuduo_1_1net_1_1_socket.md#function-listen)**()<br>abort if address in use  |
| int | **[accept](/classmuduo_1_1net_1_1_socket.md#function-accept)**([InetAddress](/class_inet_address.md) * peeraddr) |
| void | **[shutdownWrite](/classmuduo_1_1net_1_1_socket.md#function-shutdownwrite)**() |
| void | **[setTcpNoDelay](/classmuduo_1_1net_1_1_socket.md#function-settcpnodelay)**(bool on) |
| void | **[setReuseAddr](/classmuduo_1_1net_1_1_socket.md#function-setreuseaddr)**(bool on) |
| void | **[setReusePort](/classmuduo_1_1net_1_1_socket.md#function-setreuseport)**(bool on) |
| void | **[setKeepAlive](/classmuduo_1_1net_1_1_socket.md#function-setkeepalive)**(bool on) |

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


## Detailed Description

```cpp
class muduo::net::Socket;
```


Wrapper of socket file descriptor.

It closes the sockfd when desctructs. It's thread safe, all operations are delagated to OS. 

## Public Functions Documentation

### function Socket

```cpp
inline explicit Socket(
    int sockfd
)
```


### function ~Socket

```cpp
~Socket()
```


### function fd

```cpp
inline int fd() const
```


### function getTcpInfo

```cpp
bool getTcpInfo(
    struct tcp_info * tcpi
) const
```


### function getTcpInfoString

```cpp
bool getTcpInfoString(
    char * buf,
    int len
) const
```


### function bindAddress

```cpp
void bindAddress(
    const InetAddress & localaddr
)
```

abort if address in use 

### function listen

```cpp
void listen()
```

abort if address in use 

### function accept

```cpp
int accept(
    InetAddress * peeraddr
)
```


On success, returns a non-negative integer that is a descriptor for the accepted socket, which has been set to non-blocking and close-on-exec. *peeraddr is assigned. On error, -1 is returned, and *peeraddr is untouched. 


### function shutdownWrite

```cpp
void shutdownWrite()
```


### function setTcpNoDelay

```cpp
void setTcpNoDelay(
    bool on
)
```


Enable/disable TCP_NODELAY (disable/enable Nagle's algorithm). 


### function setReuseAddr

```cpp
void setReuseAddr(
    bool on
)
```


Enable/disable SO_REUSEADDR 


### function setReusePort

```cpp
void setReusePort(
    bool on
)
```


Enable/disable SO_REUSEPORT 


### function setKeepAlive

```cpp
void setKeepAlive(
    bool on
)
```


Enable/disable SO_KEEPALIVE 


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800