---
title: muduo::noncopyable

---

# muduo::noncopyable






`#include <noncopyable.h>`

Inherited by [muduo::BlockingQueue< std::pair< int, muduo::Timestamp > >](/classmuduo_1_1_blocking_queue.md), [muduo::BlockingQueue< muduo::Timestamp >](/classmuduo_1_1_blocking_queue.md), [muduo::BlockingQueue< int >](/classmuduo_1_1_blocking_queue.md), [muduo::BlockingQueue< std::string >](/classmuduo_1_1_blocking_queue.md), [muduo::BoundedBlockingQueue< std::string >](/classmuduo_1_1_bounded_blocking_queue.md), [muduo::ThreadLocal< PerThread >](/classmuduo_1_1_thread_local.md), [muduo::ThreadLocalSingleton< ConnectionList >](/classmuduo_1_1_thread_local_singleton.md), [muduo::detail::AtomicIntegerT< int32_t >](/classmuduo_1_1detail_1_1_atomic_integer_t.md), [muduo::detail::AtomicIntegerT< int64_t >](/classmuduo_1_1detail_1_1_atomic_integer_t.md), [muduo::detail::FixedBuffer< muduo::detail::kLargeBuffer >](/classmuduo_1_1detail_1_1_fixed_buffer.md), [muduo::detail::FixedBuffer< detail::kSmallBuffer >](/classmuduo_1_1detail_1_1_fixed_buffer.md), [BackendSession](/class_backend_session.md), [BackendSession](/class_backend_session.md), [Balancer](/class_balancer.md), [Balancer](/class_balancer.md), [Callback](/class_callback.md), [ChargenClient](/class_chargen_client.md), [ChatClient](/class_chat_client.md), [ChatClient](/class_chat_client.md), [ChatServer](/class_chat_server.md), [ChatServer](/class_chat_server.md), [ChatServer](/class_chat_server.md), [ChatServer](/class_chat_server.md), [Client](/class_client.md), [Client](/class_client.md), [DemuxServer](/class_demux_server.md), [DiscardClient](/class_discard_client.md), [Downloader](/class_downloader.md), [EchoClient](/class_echo_client.md), [EchoClient](/class_echo_client.md), [FastCgiCodec](/class_fast_cgi_codec.md), [Item](/class_item.md), [LengthHeaderCodec](/class_length_header_codec.md), [MemcacheServer](/class_memcache_server.md), [MultiplexServer](/class_multiplex_server.md), [Piece](/class_piece.md), [Plot](/class_plot.md), [Printer](/class_printer.md), [Printer](/class_printer.md), [Printer](/class_printer.md), [Procmon](/class_procmon.md), [ProtobufCodec](/class_protobuf_codec.md), [ProtobufDispatcherLite](/class_protobuf_dispatcher_lite.md), [QueryClient](/class_query_client.md), [QueryServer](/class_query_server.md), [RpcClient](/class_rpc_client.md), [RpcClient](/class_rpc_client.md), [RpcClient](/class_rpc_client.md), [SendThrottler](/class_send_throttler.md), [Session](/class_session.md), [Session](/class_session.md), [SudokuClient](/class_sudoku_client.md), [SudokuClient](/class_sudoku_client.md), [SudokuClient](/class_sudoku_client.md), [SudokuLoadtest](/class_sudoku_loadtest.md), [SudokuServer](/class_sudoku_server.md), [SudokuServer](/class_sudoku_server.md), [SudokuStat](/class_sudoku_stat.md), [Test](/class_test.md), [Test](/class_test.md), [Test](/class_test.md), [Test](/class_test.md), [TestNoDestroy](/class_test_no_destroy.md), [TimeClient](/class_time_client.md), [TtcpServerConnection](/class_ttcp_server_connection.md), [Tunnel](/class_tunnel.md), [UptimeClient](/class_uptime_client.md), [WordCountReceiver](/class_word_count_receiver.md), [WordCountSender](/class_word_count_sender.md), [cdns::Resolver](/classcdns_1_1_resolver.md), [curl::Curl](/classcurl_1_1_curl.md), [curl::Request](/classcurl_1_1_request.md), [hiredis::Hiredis](/classhiredis_1_1_hiredis.md), [logging::LogClient](/classlogging_1_1_log_client.md), [logging::LogServer](/classlogging_1_1_log_server.md), [logging::Session](/classlogging_1_1_session.md), [muduo::AsyncLogging](/classmuduo_1_1_async_logging.md), [muduo::BlockingQueue< T >](/classmuduo_1_1_blocking_queue.md), [muduo::BoundedBlockingQueue< T >](/classmuduo_1_1_bounded_blocking_queue.md), [muduo::Condition](/classmuduo_1_1_condition.md), [muduo::CountDownLatch](/classmuduo_1_1_count_down_latch.md), [muduo::FileUtil::AppendFile](/classmuduo_1_1_file_util_1_1_append_file.md), [muduo::FileUtil::ReadSmallFile](/classmuduo_1_1_file_util_1_1_read_small_file.md), [muduo::GzipFile](/classmuduo_1_1_gzip_file.md), [muduo::LogFile](/classmuduo_1_1_log_file.md), [muduo::LogStream](/classmuduo_1_1_log_stream.md), [muduo::MutexLockGuard](/classmuduo_1_1_mutex_lock_guard.md), [muduo::Singleton< T >](/classmuduo_1_1_singleton.md), [muduo::Thread](/classmuduo_1_1_thread.md), [muduo::ThreadLocal< T >](/classmuduo_1_1_thread_local.md), [muduo::ThreadLocalSingleton< T >](/classmuduo_1_1_thread_local_singleton.md), [muduo::ThreadPool](/classmuduo_1_1_thread_pool.md), [muduo::detail::AtomicIntegerT< T >](/classmuduo_1_1detail_1_1_atomic_integer_t.md), [muduo::detail::File](/classmuduo_1_1detail_1_1_file.md), [muduo::detail::FixedBuffer< SIZE >](/classmuduo_1_1detail_1_1_fixed_buffer.md), [muduo::net::Acceptor](/classmuduo_1_1net_1_1_acceptor.md), [muduo::net::BoilerPlate](/classmuduo_1_1net_1_1_boiler_plate.md), [muduo::net::Channel](/classmuduo_1_1net_1_1_channel.md), [muduo::net::Connector](/classmuduo_1_1net_1_1_connector.md), [muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md), [muduo::net::EventLoopThread](/classmuduo_1_1net_1_1_event_loop_thread.md), [muduo::net::EventLoopThreadPool](/classmuduo_1_1net_1_1_event_loop_thread_pool.md), [muduo::net::HttpServer](/classmuduo_1_1net_1_1_http_server.md), [muduo::net::Inspector](/classmuduo_1_1net_1_1_inspector.md), [muduo::net::PerformanceInspector](/classmuduo_1_1net_1_1_performance_inspector.md), [muduo::net::Poller](/classmuduo_1_1net_1_1_poller.md), [muduo::net::ProcessInspector](/classmuduo_1_1net_1_1_process_inspector.md), [muduo::net::ProtobufCodecLite](/classmuduo_1_1net_1_1_protobuf_codec_lite.md), [muduo::net::Socket](/classmuduo_1_1net_1_1_socket.md), [muduo::net::SystemInspector](/classmuduo_1_1net_1_1_system_inspector.md), [muduo::net::TcpClient](/classmuduo_1_1net_1_1_tcp_client.md), [muduo::net::TcpConnection](/classmuduo_1_1net_1_1_tcp_connection.md), [muduo::net::TcpServer](/classmuduo_1_1net_1_1_tcp_server.md), [muduo::net::Timer](/classmuduo_1_1net_1_1_timer.md), [muduo::net::TimerQueue](/classmuduo_1_1net_1_1_timer_queue.md), [muduo::net::ZlibInputStream](/classmuduo_1_1net_1_1_zlib_input_stream.md), [muduo::net::ZlibOutputStream](/classmuduo_1_1net_1_1_zlib_output_stream.md), [pubsub::PubSubClient](/classpubsub_1_1_pub_sub_client.md), [pubsub::PubSubServer](/classpubsub_1_1_pub_sub_server.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**(const noncopyable & ) =delete |
| void | **[operator=](/classmuduo_1_1noncopyable.md#function-operator=)**(const [noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable) & ) =delete |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**() =default |
| | **[~noncopyable](/classmuduo_1_1noncopyable.md#function-~noncopyable)**() =default |

## Public Functions Documentation

### function noncopyable

```cpp
noncopyable(
    const noncopyable & 
) =delete
```


### function operator=

```cpp
void operator=(
    const noncopyable & 
) =delete
```


## Protected Functions Documentation

### function noncopyable

```cpp
noncopyable() =default
```


### function ~noncopyable

```cpp
~noncopyable() =default
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800