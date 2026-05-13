---
title: curl::Request

---

# curl::Request






`#include <Curl.h>`

Inherits from std::enable_shared_from_this< Request >, [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void(const char *, int)> | **[DataCallback](/classcurl_1_1_request.md#typedef-datacallback)**  |
| typedef std::function< void([Request](/classcurl_1_1_request.md#function-request) *, int)> | **[DoneCallback](/classcurl_1_1_request.md#typedef-donecallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Request](/classcurl_1_1_request.md#function-request)**([Curl](/classcurl_1_1_curl.md) * owner, const char * url) |
| | **[~Request](/classcurl_1_1_request.md#function-~request)**() |
| void | **[setDataCallback](/classcurl_1_1_request.md#function-setdatacallback)**(const [DataCallback](/classcurl_1_1_request.md#typedef-datacallback) & cb) |
| void | **[setDoneCallback](/classcurl_1_1_request.md#function-setdonecallback)**(const [DoneCallback](/classcurl_1_1_request.md#typedef-donecallback) & cb) |
| void | **[setHeaderCallback](/classcurl_1_1_request.md#function-setheadercallback)**(const [DataCallback](/classcurl_1_1_request.md#typedef-datacallback) & cb) |
| void | **[headerOnly](/classcurl_1_1_request.md#function-headeronly)**() |
| void | **[setRange](/classcurl_1_1_request.md#function-setrange)**(const [muduo::StringArg](/classmuduo_1_1_string_arg.md) range) |
| template <typename OPT \> <br>int | **[setopt](/classcurl_1_1_request.md#function-setopt)**(OPT opt, long p) |
| template <typename OPT \> <br>int | **[setopt](/classcurl_1_1_request.md#function-setopt)**(OPT opt, const char * p) |
| template <typename OPT \> <br>int | **[setopt](/classcurl_1_1_request.md#function-setopt)**(OPT opt, void * p) |
| template <typename OPT \> <br>int | **[setopt](/classcurl_1_1_request.md#function-setopt)**(OPT opt, size_t(*)(char *, size_t, size_t, void *) p) |
| const char * | **[getEffectiveUrl](/classcurl_1_1_request.md#function-geteffectiveurl)**() |
| const char * | **[getRedirectUrl](/classcurl_1_1_request.md#function-getredirecturl)**() |
| int | **[getResponseCode](/classcurl_1_1_request.md#function-getresponsecode)**() |
| [muduo::net::Channel](/classmuduo_1_1net_1_1_channel.md) * | **[setChannel](/classcurl_1_1_request.md#function-setchannel)**(int fd) |
| void | **[removeChannel](/classcurl_1_1_request.md#function-removechannel)**() |
| void | **[done](/classcurl_1_1_request.md#function-done)**(int code) |
| [CURL](/_curl_8h.md#typedef-curl) * | **[getCurl](/classcurl_1_1_request.md#function-getcurl)**() |
| [muduo::net::Channel](/classmuduo_1_1net_1_1_channel.md) * | **[getChannel](/classcurl_1_1_request.md#function-getchannel)**() |

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

### typedef DataCallback

```cpp
typedef std::function<void(const char*, int)> curl::Request::DataCallback;
```


### typedef DoneCallback

```cpp
typedef std::function<void(Request*, int)> curl::Request::DoneCallback;
```


## Public Functions Documentation

### function Request

```cpp
Request(
    Curl * owner,
    const char * url
)
```


### function ~Request

```cpp
~Request()
```


### function setDataCallback

```cpp
inline void setDataCallback(
    const DataCallback & cb
)
```


### function setDoneCallback

```cpp
inline void setDoneCallback(
    const DoneCallback & cb
)
```


### function setHeaderCallback

```cpp
inline void setHeaderCallback(
    const DataCallback & cb
)
```


### function headerOnly

```cpp
void headerOnly()
```


### function setRange

```cpp
void setRange(
    const muduo::StringArg range
)
```


### function setopt

```cpp
template <typename OPT >
inline int setopt(
    OPT opt,
    long p
)
```


### function setopt

```cpp
template <typename OPT >
inline int setopt(
    OPT opt,
    const char * p
)
```


### function setopt

```cpp
template <typename OPT >
inline int setopt(
    OPT opt,
    void * p
)
```


### function setopt

```cpp
template <typename OPT >
inline int setopt(
    OPT opt,
    size_t(*)(char *, size_t, size_t, void *) p
)
```


### function getEffectiveUrl

```cpp
const char * getEffectiveUrl()
```


### function getRedirectUrl

```cpp
const char * getRedirectUrl()
```


### function getResponseCode

```cpp
int getResponseCode()
```


### function setChannel

```cpp
muduo::net::Channel * setChannel(
    int fd
)
```


### function removeChannel

```cpp
void removeChannel()
```


### function done

```cpp
void done(
    int code
)
```


### function getCurl

```cpp
inline CURL * getCurl()
```


### function getChannel

```cpp
inline muduo::net::Channel * getChannel()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800