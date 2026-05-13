---
title: examples/protobuf/codec/dispatcher_test.cc

---

# examples/protobuf/codec/dispatcher_test.cc



## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::shared_ptr< muduo::Query > | **[QueryPtr](/dispatcher__test_8cc.md#typedef-queryptr)**  |
| typedef std::shared_ptr< muduo::Answer > | **[AnswerPtr](/dispatcher__test_8cc.md#typedef-answerptr)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[test_down_pointer_cast](/dispatcher__test_8cc.md#function-test-down-pointer-cast)**() |
| void | **[onQuery](/dispatcher__test_8cc.md#function-onquery)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & , const [QueryPtr](/dispatcher__test_8cc.md#typedef-queryptr) & message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) ) |
| void | **[onAnswer](/dispatcher__test_8cc.md#function-onanswer)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & , const [AnswerPtr](/protobuf_2codec_2client_8cc.md#typedef-answerptr) & message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) ) |
| void | **[onUnknownMessageType](/dispatcher__test_8cc.md#function-onunknownmessagetype)**(const [muduo::net::TcpConnectionPtr](/namespacemuduo_1_1net.md#typedef-tcpconnectionptr) & , const [MessagePtr](/protobuf_2codec_2codec_8h.md#typedef-messageptr) & message, [muduo::Timestamp](/classmuduo_1_1_timestamp.md) ) |
| int | **[main](/dispatcher__test_8cc.md#function-main)**() |

## Types Documentation

### typedef QueryPtr

```cpp
typedef std::shared_ptr<muduo::Query> QueryPtr;
```


### typedef AnswerPtr

```cpp
typedef std::shared_ptr<muduo::Answer> AnswerPtr;
```



## Functions Documentation

### function test_down_pointer_cast

```cpp
void test_down_pointer_cast()
```


### function onQuery

```cpp
void onQuery(
    const muduo::net::TcpConnectionPtr & ,
    const QueryPtr & message,
    muduo::Timestamp 
)
```


### function onAnswer

```cpp
void onAnswer(
    const muduo::net::TcpConnectionPtr & ,
    const AnswerPtr & message,
    muduo::Timestamp 
)
```


### function onUnknownMessageType

```cpp
void onUnknownMessageType(
    const muduo::net::TcpConnectionPtr & ,
    const MessagePtr & message,
    muduo::Timestamp 
)
```


### function main

```cpp
int main()
```




## Source code

```cpp
#include "examples/protobuf/codec/dispatcher.h"

#include "examples/protobuf/codec/query.pb.h"

#include <iostream>

using std::cout;
using std::endl;

typedef std::shared_ptr<muduo::Query> QueryPtr;
typedef std::shared_ptr<muduo::Answer> AnswerPtr;

void test_down_pointer_cast()
{
  ::std::shared_ptr<google::protobuf::Message> msg(new muduo::Query);
  ::std::shared_ptr<muduo::Query> query(muduo::down_pointer_cast<muduo::Query>(msg));
  assert(msg && query);
  if (!query)
  {
    abort();
  }
}

void onQuery(const muduo::net::TcpConnectionPtr&,
             const QueryPtr& message,
             muduo::Timestamp)
{
  cout << "onQuery: " << message->GetTypeName() << endl;
}

void onAnswer(const muduo::net::TcpConnectionPtr&,
              const AnswerPtr& message,
              muduo::Timestamp)
{
  cout << "onAnswer: " << message->GetTypeName() << endl;
}

void onUnknownMessageType(const muduo::net::TcpConnectionPtr&,
                          const MessagePtr& message,
                          muduo::Timestamp)
{
  cout << "onUnknownMessageType: " << message->GetTypeName() << endl;
}

int main()
{
  GOOGLE_PROTOBUF_VERIFY_VERSION;
  test_down_pointer_cast();

  ProtobufDispatcher dispatcher(onUnknownMessageType);
  dispatcher.registerMessageCallback<muduo::Query>(onQuery);
  dispatcher.registerMessageCallback<muduo::Answer>(onAnswer);

  muduo::net::TcpConnectionPtr conn;
  muduo::Timestamp t;

  std::shared_ptr<muduo::Query> query(new muduo::Query);
  std::shared_ptr<muduo::Answer> answer(new muduo::Answer);
  std::shared_ptr<muduo::Empty> empty(new muduo::Empty);
  dispatcher.onProtobufMessage(conn, query, t);
  dispatcher.onProtobufMessage(conn, answer, t);
  dispatcher.onProtobufMessage(conn, empty, t);

  google::protobuf::ShutdownProtobufLibrary();
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
