---
title: DemuxServer

---

# DemuxServer





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DemuxServer](/class_demux_server.md#function-demuxserver)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr, const [InetAddress](/class_inet_address.md) & socksAddr) |
| void | **[start](/class_demux_server.md#function-start)**() |
| void | **[onServerConnection](/class_demux_server.md#function-onserverconnection)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[onServerMessage](/class_demux_server.md#function-onservermessage)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) ) |
| void | **[doCommand](/class_demux_server.md#function-docommand)**(const string & cmd) |
| void | **[onSocksConnection](/class_demux_server.md#function-onsocksconnection)**(int connId, const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[onSocksMessage](/class_demux_server.md#function-onsocksmessage)**(int connId, const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) ) |
| void | **[sendServerPacket](/class_demux_server.md#function-sendserverpacket)**(int connId, [Buffer](/class_buffer.md) * buf) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [EventLoop](/class_event_loop.md) * | **[loop_](/class_demux_server.md#variable-loop-)**  |
| [TcpServer](/classmuduo_1_1net_1_1_tcp_server.md) | **[server_](/class_demux_server.md#variable-server-)**  |
| [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) | **[serverConn_](/class_demux_server.md#variable-serverconn-)**  |
| const [InetAddress](/class_inet_address.md) | **[socksAddr_](/class_demux_server.md#variable-socksaddr-)**  |
| std::map< int, [Entry](/struct_entry.md) > | **[socksConns_](/class_demux_server.md#variable-socksconns-)**  |

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

### function DemuxServer

```cpp
inline DemuxServer(
    EventLoop * loop,
    const InetAddress & listenAddr,
    const InetAddress & socksAddr
)
```


### function start

```cpp
inline void start()
```


### function onServerConnection

```cpp
inline void onServerConnection(
    const TcpConnectionPtr & conn
)
```


### function onServerMessage

```cpp
inline void onServerMessage(
    const TcpConnectionPtr & conn,
    Buffer * buf,
    Timestamp 
)
```


### function doCommand

```cpp
inline void doCommand(
    const string & cmd
)
```


### function onSocksConnection

```cpp
inline void onSocksConnection(
    int connId,
    const TcpConnectionPtr & conn
)
```


### function onSocksMessage

```cpp
inline void onSocksMessage(
    int connId,
    const TcpConnectionPtr & conn,
    Buffer * buf,
    Timestamp 
)
```


### function sendServerPacket

```cpp
inline void sendServerPacket(
    int connId,
    Buffer * buf
)
```


## Public Attributes Documentation

### variable loop_

```cpp
EventLoop * loop_;
```


### variable server_

```cpp
TcpServer server_;
```


### variable serverConn_

```cpp
TcpConnectionPtr serverConn_;
```


### variable socksAddr_

```cpp
const InetAddress socksAddr_;
```


### variable socksConns_

```cpp
std::map< int, Entry > socksConns_;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800