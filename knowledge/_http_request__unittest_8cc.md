---
title: muduo/net/http/tests/HttpRequest_unittest.cc

---

# muduo/net/http/tests/HttpRequest_unittest.cc



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[HttpContext](/class_http_context.md)**  |
| class | **[HttpRequest](/class_http_request.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| | **[BOOST_AUTO_TEST_CASE](/_http_request__unittest_8cc.md#function-boost-auto-test-case)**(testParseRequestAllInOne ) |
| | **[BOOST_AUTO_TEST_CASE](/_http_request__unittest_8cc.md#function-boost-auto-test-case)**(testParseRequestInTwoPieces ) |
| | **[BOOST_AUTO_TEST_CASE](/_http_request__unittest_8cc.md#function-boost-auto-test-case)**(testParseRequestEmptyHeaderValue ) |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BOOST_TEST_MAIN](/_http_request__unittest_8cc.md#define-boost-test-main)**  |
|  | **[BOOST_TEST_DYN_LINK](/_http_request__unittest_8cc.md#define-boost-test-dyn-link)**  |


## Functions Documentation

### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testParseRequestAllInOne 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testParseRequestInTwoPieces 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testParseRequestEmptyHeaderValue 
)
```




## Macros Documentation

### define BOOST_TEST_MAIN

```cpp
#define BOOST_TEST_MAIN 
```


### define BOOST_TEST_DYN_LINK

```cpp
#define BOOST_TEST_DYN_LINK 
```


## Source code

```cpp
#include "muduo/net/http/HttpContext.h"
#include "muduo/net/Buffer.h"

//#define BOOST_TEST_MODULE BufferTest
#define BOOST_TEST_MAIN
#define BOOST_TEST_DYN_LINK
#include <boost/test/unit_test.hpp>

using muduo::string;
using muduo::Timestamp;
using muduo::net::Buffer;
using muduo::net::HttpContext;
using muduo::net::HttpRequest;

BOOST_AUTO_TEST_CASE(testParseRequestAllInOne)
{
  HttpContext context;
  Buffer input;
  input.append("GET /index.html HTTP/1.1\r\n"
       "Host: www.chenshuo.com\r\n"
       "\r\n");

  BOOST_CHECK(context.parseRequest(&input, Timestamp::now()));
  BOOST_CHECK(context.gotAll());
  const HttpRequest& request = context.request();
  BOOST_CHECK_EQUAL(request.method(), HttpRequest::kGet);
  BOOST_CHECK_EQUAL(request.path(), string("/index.html"));
  BOOST_CHECK_EQUAL(request.getVersion(), HttpRequest::kHttp11);
  BOOST_CHECK_EQUAL(request.getHeader("Host"), string("www.chenshuo.com"));
  BOOST_CHECK_EQUAL(request.getHeader("User-Agent"), string(""));
}

BOOST_AUTO_TEST_CASE(testParseRequestInTwoPieces)
{
  string all("GET /index.html HTTP/1.1\r\n"
       "Host: www.chenshuo.com\r\n"
       "\r\n");

  for (size_t sz1 = 0; sz1 < all.size(); ++sz1)
  {
    HttpContext context;
    Buffer input;
    input.append(all.c_str(), sz1);
    BOOST_CHECK(context.parseRequest(&input, Timestamp::now()));
    BOOST_CHECK(!context.gotAll());

    size_t sz2 = all.size() - sz1;
    input.append(all.c_str() + sz1, sz2);
    BOOST_CHECK(context.parseRequest(&input, Timestamp::now()));
    BOOST_CHECK(context.gotAll());
    const HttpRequest& request = context.request();
    BOOST_CHECK_EQUAL(request.method(), HttpRequest::kGet);
    BOOST_CHECK_EQUAL(request.path(), string("/index.html"));
    BOOST_CHECK_EQUAL(request.getVersion(), HttpRequest::kHttp11);
    BOOST_CHECK_EQUAL(request.getHeader("Host"), string("www.chenshuo.com"));
    BOOST_CHECK_EQUAL(request.getHeader("User-Agent"), string(""));
  }
}

BOOST_AUTO_TEST_CASE(testParseRequestEmptyHeaderValue)
{
  HttpContext context;
  Buffer input;
  input.append("GET /index.html HTTP/1.1\r\n"
       "Host: www.chenshuo.com\r\n"
       "User-Agent:\r\n"
       "Accept-Encoding: \r\n"
       "\r\n");

  BOOST_CHECK(context.parseRequest(&input, Timestamp::now()));
  BOOST_CHECK(context.gotAll());
  const HttpRequest& request = context.request();
  BOOST_CHECK_EQUAL(request.method(), HttpRequest::kGet);
  BOOST_CHECK_EQUAL(request.path(), string("/index.html"));
  BOOST_CHECK_EQUAL(request.getVersion(), HttpRequest::kHttp11);
  BOOST_CHECK_EQUAL(request.getHeader("Host"), string("www.chenshuo.com"));
  BOOST_CHECK_EQUAL(request.getHeader("User-Agent"), string(""));
  BOOST_CHECK_EQUAL(request.getHeader("Accept-Encoding"), string(""));
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
