---
title: muduo::net::sockets

---

# muduo::net::sockets



## Functions

|                | Name           |
| -------------- | -------------- |
| uint64_t | **[hostToNetwork64](/namespacemuduo_1_1net_1_1sockets.md#function-hosttonetwork64)**(uint64_t host64) |
| uint32_t | **[hostToNetwork32](/namespacemuduo_1_1net_1_1sockets.md#function-hosttonetwork32)**(uint32_t host32) |
| uint16_t | **[hostToNetwork16](/namespacemuduo_1_1net_1_1sockets.md#function-hosttonetwork16)**(uint16_t host16) |
| uint64_t | **[networkToHost64](/namespacemuduo_1_1net_1_1sockets.md#function-networktohost64)**(uint64_t net64) |
| uint32_t | **[networkToHost32](/namespacemuduo_1_1net_1_1sockets.md#function-networktohost32)**(uint32_t net32) |
| uint16_t | **[networkToHost16](/namespacemuduo_1_1net_1_1sockets.md#function-networktohost16)**(uint16_t net16) |
| const struct sockaddr * | **[sockaddr_cast](/namespacemuduo_1_1net_1_1sockets.md#function-sockaddr-cast)**(const struct sockaddr_in6 * addr) |
| int | **[createNonblockingOrDie](/namespacemuduo_1_1net_1_1sockets.md#function-createnonblockingordie)**(sa_family_t family) |
| int | **[connect](/namespacemuduo_1_1net_1_1sockets.md#function-connect)**(int sockfd, const struct sockaddr * addr) |
| void | **[bindOrDie](/namespacemuduo_1_1net_1_1sockets.md#function-bindordie)**(int sockfd, const struct sockaddr * addr) |
| void | **[listenOrDie](/namespacemuduo_1_1net_1_1sockets.md#function-listenordie)**(int sockfd) |
| int | **[accept](/namespacemuduo_1_1net_1_1sockets.md#function-accept)**(int sockfd, struct sockaddr_in6 * addr) |
| ssize_t | **[read](/namespacemuduo_1_1net_1_1sockets.md#function-read)**(int sockfd, void * buf, size_t count) |
| ssize_t | **[readv](/namespacemuduo_1_1net_1_1sockets.md#function-readv)**(int sockfd, const struct iovec * iov, int iovcnt) |
| ssize_t | **[write](/namespacemuduo_1_1net_1_1sockets.md#function-write)**(int sockfd, const void * buf, size_t count) |
| void | **[close](/namespacemuduo_1_1net_1_1sockets.md#function-close)**(int sockfd) |
| void | **[shutdownWrite](/namespacemuduo_1_1net_1_1sockets.md#function-shutdownwrite)**(int sockfd) |
| void | **[toIpPort](/namespacemuduo_1_1net_1_1sockets.md#function-toipport)**(char * buf, size_t size, const struct sockaddr * addr) |
| void | **[toIp](/namespacemuduo_1_1net_1_1sockets.md#function-toip)**(char * buf, size_t size, const struct sockaddr * addr) |
| void | **[fromIpPort](/namespacemuduo_1_1net_1_1sockets.md#function-fromipport)**(const char * ip, uint16_t port, struct sockaddr_in * addr) |
| void | **[fromIpPort](/namespacemuduo_1_1net_1_1sockets.md#function-fromipport)**(const char * ip, uint16_t port, struct sockaddr_in6 * addr) |
| int | **[getSocketError](/namespacemuduo_1_1net_1_1sockets.md#function-getsocketerror)**(int sockfd) |
| const struct sockaddr * | **[sockaddr_cast](/namespacemuduo_1_1net_1_1sockets.md#function-sockaddr-cast)**(const struct sockaddr_in * addr) |
| struct sockaddr * | **[sockaddr_cast](/namespacemuduo_1_1net_1_1sockets.md#function-sockaddr-cast)**(struct sockaddr_in6 * addr) |
| const struct sockaddr_in * | **[sockaddr_in_cast](/namespacemuduo_1_1net_1_1sockets.md#function-sockaddr-in-cast)**(const struct sockaddr * addr) |
| const struct sockaddr_in6 * | **[sockaddr_in6_cast](/namespacemuduo_1_1net_1_1sockets.md#function-sockaddr-in6-cast)**(const struct sockaddr * addr) |
| struct sockaddr_in6 | **[getLocalAddr](/namespacemuduo_1_1net_1_1sockets.md#function-getlocaladdr)**(int sockfd) |
| struct sockaddr_in6 | **[getPeerAddr](/namespacemuduo_1_1net_1_1sockets.md#function-getpeeraddr)**(int sockfd) |
| bool | **[isSelfConnect](/namespacemuduo_1_1net_1_1sockets.md#function-isselfconnect)**(int sockfd) |


## Functions Documentation

### function hostToNetwork64

```cpp
inline uint64_t hostToNetwork64(
    uint64_t host64
)
```


### function hostToNetwork32

```cpp
inline uint32_t hostToNetwork32(
    uint32_t host32
)
```


### function hostToNetwork16

```cpp
inline uint16_t hostToNetwork16(
    uint16_t host16
)
```


### function networkToHost64

```cpp
inline uint64_t networkToHost64(
    uint64_t net64
)
```


### function networkToHost32

```cpp
inline uint32_t networkToHost32(
    uint32_t net32
)
```


### function networkToHost16

```cpp
inline uint16_t networkToHost16(
    uint16_t net16
)
```


### function sockaddr_cast

```cpp
const struct sockaddr * sockaddr_cast(
    const struct sockaddr_in6 * addr
)
```


### function createNonblockingOrDie

```cpp
int createNonblockingOrDie(
    sa_family_t family
)
```


Creates a non-blocking socket file descriptor, abort if any error. 


### function connect

```cpp
int connect(
    int sockfd,
    const struct sockaddr * addr
)
```


### function bindOrDie

```cpp
void bindOrDie(
    int sockfd,
    const struct sockaddr * addr
)
```


### function listenOrDie

```cpp
void listenOrDie(
    int sockfd
)
```


### function accept

```cpp
int accept(
    int sockfd,
    struct sockaddr_in6 * addr
)
```


### function read

```cpp
ssize_t read(
    int sockfd,
    void * buf,
    size_t count
)
```


### function readv

```cpp
ssize_t readv(
    int sockfd,
    const struct iovec * iov,
    int iovcnt
)
```


### function write

```cpp
ssize_t write(
    int sockfd,
    const void * buf,
    size_t count
)
```


### function close

```cpp
void close(
    int sockfd
)
```


### function shutdownWrite

```cpp
void shutdownWrite(
    int sockfd
)
```


### function toIpPort

```cpp
void toIpPort(
    char * buf,
    size_t size,
    const struct sockaddr * addr
)
```


### function toIp

```cpp
void toIp(
    char * buf,
    size_t size,
    const struct sockaddr * addr
)
```


### function fromIpPort

```cpp
void fromIpPort(
    const char * ip,
    uint16_t port,
    struct sockaddr_in * addr
)
```


### function fromIpPort

```cpp
void fromIpPort(
    const char * ip,
    uint16_t port,
    struct sockaddr_in6 * addr
)
```


### function getSocketError

```cpp
int getSocketError(
    int sockfd
)
```


### function sockaddr_cast

```cpp
const struct sockaddr * sockaddr_cast(
    const struct sockaddr_in * addr
)
```


### function sockaddr_cast

```cpp
struct sockaddr * sockaddr_cast(
    struct sockaddr_in6 * addr
)
```


### function sockaddr_in_cast

```cpp
const struct sockaddr_in * sockaddr_in_cast(
    const struct sockaddr * addr
)
```


### function sockaddr_in6_cast

```cpp
const struct sockaddr_in6 * sockaddr_in6_cast(
    const struct sockaddr * addr
)
```


### function getLocalAddr

```cpp
struct sockaddr_in6 getLocalAddr(
    int sockfd
)
```


### function getPeerAddr

```cpp
struct sockaddr_in6 getPeerAddr(
    int sockfd
)
```


### function isSelfConnect

```cpp
bool isSelfConnect(
    int sockfd
)
```






-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800