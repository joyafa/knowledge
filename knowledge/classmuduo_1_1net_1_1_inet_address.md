---
title: muduo::net::InetAddress

---

# muduo::net::InetAddress



 [More...](#detailed-description)


`#include <InetAddress.h>`

Inherits from [muduo::copyable](/classmuduo_1_1copyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[InetAddress](/classmuduo_1_1net_1_1_inet_address.md#function-inetaddress)**(uint16_t port =0, bool loopbackOnly =false, bool ipv6 =false) |
| | **[InetAddress](/classmuduo_1_1net_1_1_inet_address.md#function-inetaddress)**([StringArg](/classmuduo_1_1_string_arg.md) ip, uint16_t port, bool ipv6 =false) |
| | **[InetAddress](/classmuduo_1_1net_1_1_inet_address.md#function-inetaddress)**(const struct sockaddr_in & addr) |
| | **[InetAddress](/classmuduo_1_1net_1_1_inet_address.md#function-inetaddress)**(const struct sockaddr_in6 & addr) |
| sa_family_t | **[family](/classmuduo_1_1net_1_1_inet_address.md#function-family)**() const |
| string | **[toIp](/classmuduo_1_1net_1_1_inet_address.md#function-toip)**() const |
| string | **[toIpPort](/classmuduo_1_1net_1_1_inet_address.md#function-toipport)**() const |
| uint16_t | **[port](/classmuduo_1_1net_1_1_inet_address.md#function-port)**() const |
| const struct sockaddr * | **[getSockAddr](/classmuduo_1_1net_1_1_inet_address.md#function-getsockaddr)**() const |
| void | **[setSockAddrInet6](/classmuduo_1_1net_1_1_inet_address.md#function-setsockaddrinet6)**(const struct sockaddr_in6 & addr6) |
| uint32_t | **[ipv4NetEndian](/classmuduo_1_1net_1_1_inet_address.md#function-ipv4netendian)**() const |
| uint16_t | **[portNetEndian](/classmuduo_1_1net_1_1_inet_address.md#function-portnetendian)**() const |
| void | **[setScopeId](/classmuduo_1_1net_1_1_inet_address.md#function-setscopeid)**(uint32_t scope_id) |
| bool | **[resolve](/classmuduo_1_1net_1_1_inet_address.md#function-resolve)**([StringArg](/classmuduo_1_1_string_arg.md) hostname, [InetAddress](/class_inet_address.md) * result) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| struct sockaddr_in | **[addr_](/classmuduo_1_1net_1_1_inet_address.md#variable-addr-)**  |
| struct sockaddr_in6 | **[addr6_](/classmuduo_1_1net_1_1_inet_address.md#variable-addr6-)**  |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Detailed Description

```cpp
class muduo::net::InetAddress;
```


Wrapper of sockaddr_in.

This is an POD interface class. 

## Public Functions Documentation

### function InetAddress

```cpp
explicit InetAddress(
    uint16_t port =0,
    bool loopbackOnly =false,
    bool ipv6 =false
)
```


Constructs an endpoint with given port number. Mostly used in [TcpServer](/classmuduo_1_1net_1_1_tcp_server.md) listening. 


### function InetAddress

```cpp
InetAddress(
    StringArg ip,
    uint16_t port,
    bool ipv6 =false
)
```


Constructs an endpoint with given ip and port. `ip` should be "1.2.3.4" 


### function InetAddress

```cpp
inline explicit InetAddress(
    const struct sockaddr_in & addr
)
```


Constructs an endpoint with given struct `sockaddr_in` Mostly used when accepting new connections 


### function InetAddress

```cpp
inline explicit InetAddress(
    const struct sockaddr_in6 & addr
)
```


### function family

```cpp
inline sa_family_t family() const
```


### function toIp

```cpp
string toIp() const
```


### function toIpPort

```cpp
string toIpPort() const
```


### function port

```cpp
uint16_t port() const
```


### function getSockAddr

```cpp
inline const struct sockaddr * getSockAddr() const
```


### function setSockAddrInet6

```cpp
inline void setSockAddrInet6(
    const struct sockaddr_in6 & addr6
)
```


### function ipv4NetEndian

```cpp
uint32_t ipv4NetEndian() const
```


### function portNetEndian

```cpp
inline uint16_t portNetEndian() const
```


### function setScopeId

```cpp
void setScopeId(
    uint32_t scope_id
)
```


### function resolve

```cpp
static bool resolve(
    StringArg hostname,
    InetAddress * result
)
```


## Public Attributes Documentation

### variable addr_

```cpp
struct sockaddr_in addr_;
```


### variable addr6_

```cpp
struct sockaddr_in6 addr6_;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800