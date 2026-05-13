---
title: muduo::net::HttpResponse

---

# muduo::net::HttpResponse






`#include <HttpResponse.h>`

Inherits from [muduo::copyable](/classmuduo_1_1copyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[HttpStatusCode](/classmuduo_1_1net_1_1_http_response.md#enum-httpstatuscode)** { kUnknown, k200Ok = 200, k301MovedPermanently = 301, k400BadRequest = 400, k404NotFound = 404} |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HttpResponse](/classmuduo_1_1net_1_1_http_response.md#function-httpresponse)**(bool close) |
| void | **[setStatusCode](/classmuduo_1_1net_1_1_http_response.md#function-setstatuscode)**([HttpStatusCode](/classmuduo_1_1net_1_1_http_response.md#enum-httpstatuscode) code) |
| void | **[setStatusMessage](/classmuduo_1_1net_1_1_http_response.md#function-setstatusmessage)**(const string & message) |
| void | **[setCloseConnection](/classmuduo_1_1net_1_1_http_response.md#function-setcloseconnection)**(bool on) |
| bool | **[closeConnection](/classmuduo_1_1net_1_1_http_response.md#function-closeconnection)**() const |
| void | **[setContentType](/classmuduo_1_1net_1_1_http_response.md#function-setcontenttype)**(const string & contentType) |
| void | **[addHeader](/classmuduo_1_1net_1_1_http_response.md#function-addheader)**(const string & key, const string & value) |
| void | **[setBody](/classmuduo_1_1net_1_1_http_response.md#function-setbody)**(const string & body) |
| void | **[appendToBuffer](/classmuduo_1_1net_1_1_http_response.md#function-appendtobuffer)**([Buffer](/class_buffer.md) * output) const |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Public Types Documentation

### enum HttpStatusCode

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kUnknown | |   |
| k200Ok | 200|   |
| k301MovedPermanently | 301|   |
| k400BadRequest | 400|   |
| k404NotFound | 404|   |




## Public Functions Documentation

### function HttpResponse

```cpp
inline explicit HttpResponse(
    bool close
)
```


### function setStatusCode

```cpp
inline void setStatusCode(
    HttpStatusCode code
)
```


### function setStatusMessage

```cpp
inline void setStatusMessage(
    const string & message
)
```


### function setCloseConnection

```cpp
inline void setCloseConnection(
    bool on
)
```


### function closeConnection

```cpp
inline bool closeConnection() const
```


### function setContentType

```cpp
inline void setContentType(
    const string & contentType
)
```


### function addHeader

```cpp
inline void addHeader(
    const string & key,
    const string & value
)
```


### function setBody

```cpp
inline void setBody(
    const string & body
)
```


### function appendToBuffer

```cpp
void appendToBuffer(
    Buffer * output
) const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800