---
title: muduo::net::HttpRequest

---

# muduo::net::HttpRequest






`#include <HttpRequest.h>`

Inherits from [muduo::copyable](/classmuduo_1_1copyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[Method](/classmuduo_1_1net_1_1_http_request.md#enum-method)** { kInvalid, kGet, kPost, kHead, kPut, kDelete} |
| enum| **[Version](/classmuduo_1_1net_1_1_http_request.md#enum-version)** { kUnknown, kHttp10, kHttp11} |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[HttpRequest](/classmuduo_1_1net_1_1_http_request.md#function-httprequest)**() |
| void | **[setVersion](/classmuduo_1_1net_1_1_http_request.md#function-setversion)**([Version](/classmuduo_1_1net_1_1_http_request.md#enum-version) v) |
| [Version](/classmuduo_1_1net_1_1_http_request.md#enum-version) | **[getVersion](/classmuduo_1_1net_1_1_http_request.md#function-getversion)**() const |
| bool | **[setMethod](/classmuduo_1_1net_1_1_http_request.md#function-setmethod)**(const char * start, const char * end) |
| [Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) | **[method](/classmuduo_1_1net_1_1_http_request.md#function-method)**() const |
| const char * | **[methodString](/classmuduo_1_1net_1_1_http_request.md#function-methodstring)**() const |
| void | **[setPath](/classmuduo_1_1net_1_1_http_request.md#function-setpath)**(const char * start, const char * end) |
| const string & | **[path](/classmuduo_1_1net_1_1_http_request.md#function-path)**() const |
| void | **[setQuery](/classmuduo_1_1net_1_1_http_request.md#function-setquery)**(const char * start, const char * end) |
| const string & | **[query](/classmuduo_1_1net_1_1_http_request.md#function-query)**() const |
| void | **[setReceiveTime](/classmuduo_1_1net_1_1_http_request.md#function-setreceivetime)**([Timestamp](/class_timestamp.md) t) |
| [Timestamp](/class_timestamp.md) | **[receiveTime](/classmuduo_1_1net_1_1_http_request.md#function-receivetime)**() const |
| void | **[addHeader](/classmuduo_1_1net_1_1_http_request.md#function-addheader)**(const char * start, const char * colon, const char * end) |
| string | **[getHeader](/classmuduo_1_1net_1_1_http_request.md#function-getheader)**(const string & field) const |
| const std::map< string, string > & | **[headers](/classmuduo_1_1net_1_1_http_request.md#function-headers)**() const |
| void | **[swap](/classmuduo_1_1net_1_1_http_request.md#function-swap)**([HttpRequest](/class_http_request.md) & that) |

## Additional inherited members

**Protected Functions inherited from [muduo::copyable](/classmuduo_1_1copyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[copyable](/classmuduo_1_1copyable.md#function-copyable)**() =default |
| | **[~copyable](/classmuduo_1_1copyable.md#function-~copyable)**() =default |


## Public Types Documentation

### enum Method

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kInvalid | |   |
| kGet | |   |
| kPost | |   |
| kHead | |   |
| kPut | |   |
| kDelete | |   |




### enum Version

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kUnknown | |   |
| kHttp10 | |   |
| kHttp11 | |   |




## Public Functions Documentation

### function HttpRequest

```cpp
inline HttpRequest()
```


### function setVersion

```cpp
inline void setVersion(
    Version v
)
```


### function getVersion

```cpp
inline Version getVersion() const
```


### function setMethod

```cpp
inline bool setMethod(
    const char * start,
    const char * end
)
```


### function method

```cpp
inline Method method() const
```


### function methodString

```cpp
inline const char * methodString() const
```


### function setPath

```cpp
inline void setPath(
    const char * start,
    const char * end
)
```


### function path

```cpp
inline const string & path() const
```


### function setQuery

```cpp
inline void setQuery(
    const char * start,
    const char * end
)
```


### function query

```cpp
inline const string & query() const
```


### function setReceiveTime

```cpp
inline void setReceiveTime(
    Timestamp t
)
```


### function receiveTime

```cpp
inline Timestamp receiveTime() const
```


### function addHeader

```cpp
inline void addHeader(
    const char * start,
    const char * colon,
    const char * end
)
```


### function getHeader

```cpp
inline string getHeader(
    const string & field
) const
```


### function headers

```cpp
inline const std::map< string, string > & headers() const
```


### function swap

```cpp
inline void swap(
    HttpRequest & that
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800