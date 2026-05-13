---
title: examples/protobuf/codec/client.cc

---

# examples/protobuf/codec/client.cc



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[QueryClient](/class_query_client.md)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::shared_ptr< muduo::Empty > | **[EmptyPtr](/protobuf_2codec_2client_8cc.md#typedef-emptyptr)**  |
| typedef std::shared_ptr< muduo::Answer > | **[AnswerPtr](/protobuf_2codec_2client_8cc.md#typedef-answerptr)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/protobuf_2codec_2client_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| google::protobuf::Message * | **[messageToSend](/protobuf_2codec_2client_8cc.md#variable-messagetosend)**  |

## Types Documentation

### typedef EmptyPtr

```cpp
typedef std::shared_ptr<muduo::Empty> EmptyPtr;
```


### typedef AnswerPtr

```cpp
typedef std::shared_ptr<muduo::Answer> AnswerPtr;
```



## Functions Documentation

### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```



## Attributes Documentation

### variable messageToSend

```cpp
google::protobuf::Message * messageToSend;
```



## Source code

```cpp
#include "examples/protobuf/codec/dispatcher.h"
#include "examples/protobuf/codec/codec.h"
#include "examples/protobuf/codec/query.pb.h"

#include "muduo/base/Logging.h"
#include "muduo/base/Mutex.h"
#include "muduo/net/EventLoop.h"
#include "muduo/net/TcpClient.h"

#include <stdio.h>
#include <unistd.h>

using namespace muduo;
using namespace muduo::net;

typedef std::shared_ptr<muduo::Empty> EmptyPtr;
typedef std::shared_ptr<muduo::Answer> AnswerPtr;

google::protobuf::Message* messageToSend;

class QueryClient : noncopyable
{
 public:
  QueryClient(EventLoop* loop,
              const InetAddress& serverAddr)
  : loop_(loop),
    client_(loop, serverAddr, "QueryClient"),
    dispatcher_(std::bind(&QueryClient::onUnknownMessage, this, _1, _2, _3)),
    codec_(std::bind(&ProtobufDispatcher::onProtobufMessage, &dispatcher_, _1, _2, _3))
  {
    dispatcher_.registerMessageCallback<muduo::Answer>(
        std::bind(&QueryClient::onAnswer, this, _1, _2, _3));
    dispatcher_.registerMessageCallback<muduo::Empty>(
        std::bind(&QueryClient::onEmpty, this, _1, _2, _3));
    client_.setConnectionCallback(
        std::bind(&QueryClient::onConnection, this, _1));
    client_.setMessageCallback(
        std::bind(&ProtobufCodec::onMessage, &codec_, _1, _2, _3));
  }

  void connect()
  {
    client_.connect();
  }

 private:

  void onConnection(const TcpConnectionPtr& conn)
  {
    LOG_INFO << conn->localAddress().toIpPort() << " -> "
        << conn->peerAddress().toIpPort() << " is "
        << (conn->connected() ? "UP" : "DOWN");

    if (conn->connected())
    {
      codec_.send(conn, *messageToSend);
    }
    else
    {
      loop_->quit();
    }
  }

  void onUnknownMessage(const TcpConnectionPtr&,
                        const MessagePtr& message,
                        Timestamp)
  {
    LOG_INFO << "onUnknownMessage: " << message->GetTypeName();
  }

  void onAnswer(const muduo::net::TcpConnectionPtr&,
                const AnswerPtr& message,
                muduo::Timestamp)
  {
    LOG_INFO << "onAnswer:\n" << message->GetTypeName() << message->DebugString();
  }

  void onEmpty(const muduo::net::TcpConnectionPtr&,
               const EmptyPtr& message,
               muduo::Timestamp)
  {
    LOG_INFO << "onEmpty: " << message->GetTypeName();
  }

  EventLoop* loop_;
  TcpClient client_;
  ProtobufDispatcher dispatcher_;
  ProtobufCodec codec_;
};

int main(int argc, char* argv[])
{
  LOG_INFO << "pid = " << getpid();
  if (argc > 2)
  {
    EventLoop loop;
    uint16_t port = static_cast<uint16_t>(atoi(argv[2]));
    InetAddress serverAddr(argv[1], port);

    muduo::Query query;
    query.set_id(1);
    query.set_questioner("Chen Shuo");
    query.add_question("Running?");
    muduo::Empty empty;
    messageToSend = &query;

    if (argc > 3 && argv[3][0] == 'e')
    {
      messageToSend = &empty;
    }

    QueryClient client(&loop, serverAddr);
    client.connect();
    loop.loop();
  }
  else
  {
    printf("Usage: %s host_ip port [q|e]\n", argv[0]);
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
