---
title: curl::Curl

---

# curl::Curl






`#include <Curl.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[Option](/classcurl_1_1_curl.md#enum-option)** { kCURLnossl = 0, kCURLssl = 1} |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Curl](/classcurl_1_1_curl.md#function-curl)**([muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * loop) |
| | **[~Curl](/classcurl_1_1_curl.md#function-~curl)**() |
| [RequestPtr](/namespacecurl.md#typedef-requestptr) | **[getUrl](/classcurl_1_1_curl.md#function-geturl)**([muduo::StringArg](/classmuduo_1_1_string_arg.md) url) |
| [CURLM](/_curl_8h.md#typedef-curlm) * | **[getCurlm](/classcurl_1_1_curl.md#function-getcurlm)**() |
| [muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * | **[getLoop](/classcurl_1_1_curl.md#function-getloop)**() |
| void | **[initialize](/classcurl_1_1_curl.md#function-initialize)**([Option](/classcurl_1_1_curl.md#enum-option) opt =[kCURLnossl](/classcurl_1_1_curl.md#enumvalue-kcurlnossl)) |

## Additional inherited members

**Public Functions inherited from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**(const noncopyable & ) =delete |
| void | **[operator=](/classmuduo_1_1noncopyable.md#function-operator=)**(const [noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable) & ) =delete |

**Protected Functions inherited from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)**

|                | Name           |
| -------------- | -------------- |
| | **[noncopyable](/classmuduo_1_1noncopyable.md#function-noncopyable)**() =default |
| | **[~noncopyable](/classmuduo_1_1noncopyable.md#function-~noncopyable)**() =default |


## Public Types Documentation

### enum Option

| Enumerator | Value | Description |
| ---------- | ----- | ----------- |
| kCURLnossl | 0|   |
| kCURLssl | 1|   |




## Public Functions Documentation

### function Curl

```cpp
explicit Curl(
    muduo::net::EventLoop * loop
)
```


### function ~Curl

```cpp
~Curl()
```


### function getUrl

```cpp
RequestPtr getUrl(
    muduo::StringArg url
)
```


### function getCurlm

```cpp
inline CURLM * getCurlm()
```


### function getLoop

```cpp
inline muduo::net::EventLoop * getLoop()
```


### function initialize

```cpp
static void initialize(
    Option opt =kCURLnossl
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800