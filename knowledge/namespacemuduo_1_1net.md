---
title: muduo::net

---

# muduo::net

 [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[muduo::net::detail](/namespacemuduo_1_1net_1_1detail.md)**  |
| **[muduo::net::sockets](/namespacemuduo_1_1net_1_1sockets.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::net::Acceptor](/classmuduo_1_1net_1_1_acceptor.md)**  |
| class | **[muduo::net::BoilerPlate](/classmuduo_1_1net_1_1_boiler_plate.md)**  |
| class | **[muduo::net::Buffer](/classmuduo_1_1net_1_1_buffer.md)**  |
| class | **[muduo::net::BufferOutputStream](/classmuduo_1_1net_1_1_buffer_output_stream.md)**  |
| class | **[muduo::net::Channel](/classmuduo_1_1net_1_1_channel.md)**  |
| class | **[muduo::net::Connector](/classmuduo_1_1net_1_1_connector.md)**  |
| class | **[muduo::net::EPollPoller](/classmuduo_1_1net_1_1_e_poll_poller.md)**  |
| class | **[muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md)**  |
| class | **[muduo::net::EventLoopThread](/classmuduo_1_1net_1_1_event_loop_thread.md)**  |
| class | **[muduo::net::EventLoopThreadPool](/classmuduo_1_1net_1_1_event_loop_thread_pool.md)**  |
| class | **[muduo::net::HttpContext](/classmuduo_1_1net_1_1_http_context.md)**  |
| class | **[muduo::net::HttpRequest](/classmuduo_1_1net_1_1_http_request.md)**  |
| class | **[muduo::net::HttpResponse](/classmuduo_1_1net_1_1_http_response.md)**  |
| class | **[muduo::net::HttpServer](/classmuduo_1_1net_1_1_http_server.md)**  |
| class | **[muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md)**  |
| class | **[muduo::net::Inspector](/classmuduo_1_1net_1_1_inspector.md)**  |
| class | **[muduo::net::PerformanceInspector](/classmuduo_1_1net_1_1_performance_inspector.md)**  |
| class | **[muduo::net::Poller](/classmuduo_1_1net_1_1_poller.md)**  |
| class | **[muduo::net::PollPoller](/classmuduo_1_1net_1_1_poll_poller.md)**  |
| class | **[muduo::net::ProcessInspector](/classmuduo_1_1net_1_1_process_inspector.md)**  |
| class | **[muduo::net::ProtobufCodecLite](/classmuduo_1_1net_1_1_protobuf_codec_lite.md)**  |
| class | **[muduo::net::ProtobufCodecLiteT](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md)**  |
| class | **[muduo::net::RpcChannel](/classmuduo_1_1net_1_1_rpc_channel.md)**  |
| class | **[muduo::net::RpcServer](/classmuduo_1_1net_1_1_rpc_server.md)**  |
| class | **[muduo::net::Socket](/classmuduo_1_1net_1_1_socket.md)**  |
| class | **[muduo::net::SystemInspector](/classmuduo_1_1net_1_1_system_inspector.md)**  |
| class | **[muduo::net::TcpClient](/classmuduo_1_1net_1_1_tcp_client.md)**  |
| class | **[muduo::net::TcpConnection](/classmuduo_1_1net_1_1_tcp_connection.md)**  |
| class | **[muduo::net::TcpServer](/classmuduo_1_1net_1_1_tcp_server.md)**  |
| class | **[muduo::net::Timer](/classmuduo_1_1net_1_1_timer.md)**  |
| class | **[muduo::net::TimerId](/classmuduo_1_1net_1_1_timer_id.md)**  |
| class | **[muduo::net::TimerQueue](/classmuduo_1_1net_1_1_timer_queue.md)**  |
| class | **[muduo::net::ZlibInputStream](/classmuduo_1_1net_1_1_zlib_input_stream.md)**  |
| class | **[muduo::net::ZlibOutputStream](/classmuduo_1_1net_1_1_zlib_output_stream.md)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::shared_ptr< [TcpConnection](/classmuduo_1_1net_1_1_tcp_connection.md) > | **[TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr)**  |
| typedef std::function< void()> | **[TimerCallback](/namespacemuduo_1_1net.md#typedef-timercallback)**  |
| typedef std::function< void(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &)> | **[ConnectionCallback](/namespacemuduo_1_1net.md#typedef-connectioncallback)**  |
| typedef std::function< void(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &)> | **[CloseCallback](/namespacemuduo_1_1net.md#typedef-closecallback)**  |
| typedef std::function< void(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &)> | **[WriteCompleteCallback](/namespacemuduo_1_1net.md#typedef-writecompletecallback)**  |
| typedef std::function< void(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, size_t)> | **[HighWaterMarkCallback](/namespacemuduo_1_1net.md#typedef-highwatermarkcallback)**  |
| typedef std::function< void(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) &, [Buffer](/class_buffer.md) *, [Timestamp](/class_timestamp.md))> | **[MessageCallback](/namespacemuduo_1_1net.md#typedef-messagecallback)**  |
| typedef std::shared_ptr< google::protobuf::Message > | **[MessagePtr](/namespacemuduo_1_1net.md#typedef-messageptr)**  |
| typedef std::shared_ptr< [RpcChannel](/classmuduo_1_1net_1_1_rpc_channel.md) > | **[RpcChannelPtr](/namespacemuduo_1_1net.md#typedef-rpcchannelptr)**  |
| typedef std::shared_ptr< RpcMessage > | **[RpcMessagePtr](/namespacemuduo_1_1net.md#typedef-rpcmessageptr)**  |
| typedef [ProtobufCodecLiteT](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md)< RpcMessage, [rpctag](/namespacemuduo_1_1net.md#variable-rpctag) > | **[RpcCodec](/namespacemuduo_1_1net.md#typedef-rpccodec)**  |
| typedef std::shared_ptr< [Connector](/classmuduo_1_1net_1_1_connector.md) > | **[ConnectorPtr](/namespacemuduo_1_1net.md#typedef-connectorptr)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[defaultConnectionCallback](/namespacemuduo_1_1net.md#function-defaultconnectioncallback)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn) |
| void | **[defaultMessageCallback](/namespacemuduo_1_1net.md#function-defaultmessagecallback)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & conn, [Buffer](/class_buffer.md) * buffer, [Timestamp](/class_timestamp.md) receiveTime) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const char[] | **[rpctag](/namespacemuduo_1_1net.md#variable-rpctag)**  |

## Detailed Description


TCP networking. 

## Types Documentation

### typedef TcpConnectionPtr

```cpp
typedef std::shared_ptr< TcpConnection > muduo::net::TcpConnectionPtr;
```


### typedef TimerCallback

```cpp
typedef std::function<void()> muduo::net::TimerCallback;
```


### typedef ConnectionCallback

```cpp
typedef std::function<void (const TcpConnectionPtr&)> muduo::net::ConnectionCallback;
```


### typedef CloseCallback

```cpp
typedef std::function<void (const TcpConnectionPtr&)> muduo::net::CloseCallback;
```


### typedef WriteCompleteCallback

```cpp
typedef std::function<void (const TcpConnectionPtr&)> muduo::net::WriteCompleteCallback;
```


### typedef HighWaterMarkCallback

```cpp
typedef std::function<void (const TcpConnectionPtr&, size_t)> muduo::net::HighWaterMarkCallback;
```


### typedef MessageCallback

```cpp
typedef std::function<void (const TcpConnectionPtr&, Buffer*, Timestamp)> muduo::net::MessageCallback;
```


### typedef MessagePtr

```cpp
typedef std::shared_ptr<google::protobuf::Message> muduo::net::MessagePtr;
```


### typedef RpcChannelPtr

```cpp
typedef std::shared_ptr<RpcChannel> muduo::net::RpcChannelPtr;
```


### typedef RpcMessagePtr

```cpp
typedef std::shared_ptr<RpcMessage> muduo::net::RpcMessagePtr;
```


### typedef RpcCodec

```cpp
typedef ProtobufCodecLiteT<RpcMessage, rpctag> muduo::net::RpcCodec;
```


### typedef ConnectorPtr

```cpp
typedef std::shared_ptr<Connector> muduo::net::ConnectorPtr;
```



## Functions Documentation

### function defaultConnectionCallback

```cpp
void defaultConnectionCallback(
    const TcpConnectionPtr & conn
)
```


### function defaultMessageCallback

```cpp
void defaultMessageCallback(
    const TcpConnectionPtr & conn,
    Buffer * buffer,
    Timestamp receiveTime
)
```



## Attributes Documentation

### variable rpctag

```cpp
const char[] rpctag = "RPC0";
```





-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800