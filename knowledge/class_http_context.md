---
title: HttpContext

---

# HttpContext






`#include <HttpContext.h>`

Inherits from [muduo::copyable](/classmuduo_1_1copyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[HttpRequestParseState](/class_http_context.md#enum-httprequestparsestate)** { kExpectRequestLine, kExpectHeaders, kExpectBody, kGotAll} |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HttpContext](/class_http_context.md#function-httpcontext)**() |
| bool | **[parseRequest](/class_http_context.md#function-parserequest)**([Buffer](/class_buffer.md) * buf, [Timestamp](/class_timestamp.md) receiveTime) |
| bool | **[gotAll](/class_http_context.md#function-gotall)**() const |
| void | **[reset](/class_http_context.md#function-reset)**() |
| const [HttpRequest](/class_http_request.md) & | **[request](/class_http_context.md#function-request)**() const |
| [HttpRequest](/class_http_request.md) & | **[request](/class_http_context.md#function-request)**() |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Public Types Documentation

### enum HttpRequestParseState

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kExpectRequestLine | |   |
| kExpectHeaders | |   |
| kExpectBody | |   |
| kGotAll | |   |




## Public Functions Documentation

### function HttpContext

```cpp
inline HttpContext()
```


### function parseRequest

```cpp
bool parseRequest(
    Buffer * buf,
    Timestamp receiveTime
)
```


### function gotAll

```cpp
inline bool gotAll() const
```


### function reset

```cpp
inline void reset()
```


### function request

```cpp
inline const HttpRequest & request() const
```


### function request

```cpp
inline HttpRequest & request()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800