---
title: muduo/net/protorpc/RpcCodec_test.cc

---

# muduo/net/protorpc/RpcCodec_test.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[rpcMessageCallback](/_rpc_codec__test_8cc.md#function-rpcmessagecallback)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & , const [RpcMessagePtr](/namespacemuduo_1_1net.md#typedef-rpcmessageptr) & , [Timestamp](/class_timestamp.md) ) |
| void | **[messageCallback](/_rpc_codec__test_8cc.md#function-messagecallback)**(const [TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & , const [MessagePtr](/protobuf_2codec_2codec_8h.md#typedef-messageptr) & msg, [Timestamp](/class_timestamp.md) ) |
| void | **[print](/_rpc_codec__test_8cc.md#function-print)**(const [Buffer](/class_buffer.md) & buf) |
| int | **[main](/_rpc_codec__test_8cc.md#function-main)**() |

## Attributes

|                | Name           |
| -------------- | -------------- |
| [MessagePtr](/protobuf_2codec_2codec_8h.md#typedef-messageptr) | **[g_msgptr](/_rpc_codec__test_8cc.md#variable-g-msgptr)**  |
| char[] | **[rpctag](/_rpc_codec__test_8cc.md#variable-rpctag)**  |


## Functions Documentation

### function rpcMessageCallback

```cpp
void rpcMessageCallback(
    const TcpConnectionPtr & ,
    const RpcMessagePtr & ,
    Timestamp 
)
```


### function messageCallback

```cpp
void messageCallback(
    const TcpConnectionPtr & ,
    const MessagePtr & msg,
    Timestamp 
)
```


### function print

```cpp
void print(
    const Buffer & buf
)
```


### function main

```cpp
int main()
```



## Attributes Documentation

### variable g_msgptr

```cpp
MessagePtr g_msgptr;
```


### variable rpctag

```cpp
char[] rpctag = "RPC0";
```



## Source code

```cpp
#undef NDEBUG
#include "muduo/net/protorpc/RpcCodec.h"
#include "muduo/net/protorpc/rpc.pb.h"
#include "muduo/net/protobuf/ProtobufCodecLite.h"
#include "muduo/net/Buffer.h"

#include <stdio.h>

using namespace muduo;
using namespace muduo::net;

void rpcMessageCallback(const TcpConnectionPtr&,
                        const RpcMessagePtr&,
                        Timestamp)
{
}

MessagePtr g_msgptr;
void messageCallback(const TcpConnectionPtr&,
                     const MessagePtr& msg,
                     Timestamp)
{
  g_msgptr = msg;
}

void print(const Buffer& buf)
{
  printf("encoded to %zd bytes\n", buf.readableBytes());
  for (size_t i = 0; i < buf.readableBytes(); ++i)
  {
    unsigned char ch = static_cast<unsigned char>(buf.peek()[i]);

    printf("%2zd:  0x%02x  %c\n", i, ch, isgraph(ch) ? ch : ' ');
  }
}

char rpctag[] = "RPC0";

int main()
{
  RpcMessage message;
  message.set_type(REQUEST);
  message.set_id(2);
  char wire[] = "\0\0\0\x13" "RPC0" "\x08\x01\x11\x02\0\0\0\0\0\0\0" "\x0f\xef\x01\x32";
  string expected(wire, sizeof(wire)-1);
  string s1, s2;
  Buffer buf1, buf2;
  {
  RpcCodec codec(rpcMessageCallback);
  codec.fillEmptyBuffer(&buf1, message);
  print(buf1);
  s1 = buf1.toStringPiece().as_string();
  }

  {
  ProtobufCodecLite codec(&RpcMessage::default_instance(), "RPC0", messageCallback);
  codec.fillEmptyBuffer(&buf2, message);
  print(buf2);
  s2 = buf2.toStringPiece().as_string();
  codec.onMessage(TcpConnectionPtr(), &buf1, Timestamp::now());
  assert(g_msgptr);
  assert(g_msgptr->DebugString() == message.DebugString());
  g_msgptr.reset();
  }
  assert(s1 == s2);
  assert(s1 == expected);
  assert(s2 == expected);

  {
  Buffer buf;
  ProtobufCodecLite codec(&RpcMessage::default_instance(), "XYZ", messageCallback);
  codec.fillEmptyBuffer(&buf, message);
  print(buf);
  s2 = buf.toStringPiece().as_string();
  codec.onMessage(TcpConnectionPtr(), &buf, Timestamp::now());
  assert(g_msgptr);
  assert(g_msgptr->DebugString() == message.DebugString());
  }

  google::protobuf::ShutdownProtobufLibrary();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
