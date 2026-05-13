---
title: muduo/net/tests/ZlibStream_unittest.cc

---

# muduo/net/tests/ZlibStream_unittest.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| | **[BOOST_AUTO_TEST_CASE](/_zlib_stream__unittest_8cc.md#function-boost-auto-test-case)**(testZlibOutputStream ) |
| | **[BOOST_AUTO_TEST_CASE](/_zlib_stream__unittest_8cc.md#function-boost-auto-test-case)**(testZlibOutputStream1 ) |
| | **[BOOST_AUTO_TEST_CASE](/_zlib_stream__unittest_8cc.md#function-boost-auto-test-case)**(testZlibOutputStream2 ) |
| | **[BOOST_AUTO_TEST_CASE](/_zlib_stream__unittest_8cc.md#function-boost-auto-test-case)**(testZlibOutputStream3 ) |
| | **[BOOST_AUTO_TEST_CASE](/_zlib_stream__unittest_8cc.md#function-boost-auto-test-case)**(testZlibOutputStream4 ) |
| | **[BOOST_AUTO_TEST_CASE](/_zlib_stream__unittest_8cc.md#function-boost-auto-test-case)**(testZlibOutputStream5 ) |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[BOOST_TEST_MAIN](/_zlib_stream__unittest_8cc.md#define-boost-test-main)**  |
|  | **[BOOST_TEST_DYN_LINK](/_zlib_stream__unittest_8cc.md#define-boost-test-dyn-link)**  |


## Functions Documentation

### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testZlibOutputStream 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testZlibOutputStream1 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testZlibOutputStream2 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testZlibOutputStream3 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testZlibOutputStream4 
)
```


### function BOOST_AUTO_TEST_CASE

```cpp
BOOST_AUTO_TEST_CASE(
    testZlibOutputStream5 
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
#include "muduo/net/ZlibStream.h"

#include "muduo/base/Logging.h"

#define BOOST_TEST_MAIN
#define BOOST_TEST_DYN_LINK
#include <boost/test/unit_test.hpp>

#include <stdio.h>

BOOST_AUTO_TEST_CASE(testZlibOutputStream)
{
  muduo::net::Buffer output;
  {
    muduo::net::ZlibOutputStream stream(&output);
    BOOST_CHECK_EQUAL(output.readableBytes(), 0);
  }
  BOOST_CHECK_EQUAL(output.readableBytes(), 8);
}

BOOST_AUTO_TEST_CASE(testZlibOutputStream1)
{
  muduo::net::Buffer output;
  muduo::net::ZlibOutputStream stream(&output);
  BOOST_CHECK_EQUAL(stream.zlibErrorCode(), Z_OK);
  stream.finish();
  BOOST_CHECK_EQUAL(stream.zlibErrorCode(), Z_STREAM_END);
}

BOOST_AUTO_TEST_CASE(testZlibOutputStream2)
{
  muduo::net::Buffer output;
  muduo::net::ZlibOutputStream stream(&output);
  BOOST_CHECK_EQUAL(stream.zlibErrorCode(), Z_OK);
  BOOST_CHECK(stream.write("01234567890123456789012345678901234567890123456789"));
  stream.finish();
  // printf("%zd\n", output.readableBytes());
  BOOST_CHECK_EQUAL(stream.zlibErrorCode(), Z_STREAM_END);
}

BOOST_AUTO_TEST_CASE(testZlibOutputStream3)
{
  muduo::net::Buffer output;
  muduo::net::ZlibOutputStream stream(&output);
  BOOST_CHECK_EQUAL(stream.zlibErrorCode(), Z_OK);
  for (int i = 0; i < 1024*1024; ++i)
  {
    BOOST_CHECK(stream.write("01234567890123456789012345678901234567890123456789"));
  }
  stream.finish();
  // printf("total %zd\n", output.readableBytes());
  BOOST_CHECK_EQUAL(stream.zlibErrorCode(), Z_STREAM_END);
}

BOOST_AUTO_TEST_CASE(testZlibOutputStream4)
{
  muduo::net::Buffer output;
  muduo::net::ZlibOutputStream stream(&output);
  BOOST_CHECK_EQUAL(stream.zlibErrorCode(), Z_OK);
  muduo::string input;
  for (int i = 0; i < 32768; ++i)
  {
    input += "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-"[rand() % 64];
  }

  for (int i = 0; i < 10; ++i)
  {
    BOOST_CHECK(stream.write(input));
  }
  stream.finish();
  // printf("total %zd\n", output.readableBytes());
  BOOST_CHECK_EQUAL(stream.zlibErrorCode(), Z_STREAM_END);
}

BOOST_AUTO_TEST_CASE(testZlibOutputStream5)
{
  muduo::net::Buffer output;
  muduo::net::ZlibOutputStream stream(&output);
  BOOST_CHECK_EQUAL(stream.zlibErrorCode(), Z_OK);
  muduo::string input(1024*1024, '_');
  for (int i = 0; i < 64; ++i)
  {
    BOOST_CHECK(stream.write(input));
  }
  printf("bufsiz %d\n", stream.internalOutputBufferSize());
  LOG_INFO << "total_in " << stream.inputBytes();
  LOG_INFO << "total_out " << stream.outputBytes();
  stream.finish();
  printf("total %zd\n", output.readableBytes());
  BOOST_CHECK_EQUAL(stream.zlibErrorCode(), Z_STREAM_END);
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
