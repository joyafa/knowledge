---
title: muduo::net::PerformanceInspector

---

# muduo::net::PerformanceInspector






`#include <PerformanceInspector.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[registerCommands](/classmuduo_1_1net_1_1_performance_inspector.md#function-registercommands)**([Inspector](/classmuduo_1_1net_1_1_inspector.md) * ins) |
| string | **[heap](/classmuduo_1_1net_1_1_performance_inspector.md#function-heap)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[growth](/classmuduo_1_1net_1_1_performance_inspector.md#function-growth)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[profile](/classmuduo_1_1net_1_1_performance_inspector.md#function-profile)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[cmdline](/classmuduo_1_1net_1_1_performance_inspector.md#function-cmdline)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[memstats](/classmuduo_1_1net_1_1_performance_inspector.md#function-memstats)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[memhistogram](/classmuduo_1_1net_1_1_performance_inspector.md#function-memhistogram)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[releaseFreeMemory](/classmuduo_1_1net_1_1_performance_inspector.md#function-releasefreememory)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[symbol](/classmuduo_1_1net_1_1_performance_inspector.md#function-symbol)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |

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


## Public Functions Documentation

### function registerCommands

```cpp
void registerCommands(
    Inspector * ins
)
```


### function heap

```cpp
static string heap(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function growth

```cpp
static string growth(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function profile

```cpp
static string profile(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function cmdline

```cpp
static string cmdline(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function memstats

```cpp
static string memstats(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function memhistogram

```cpp
static string memhistogram(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function releaseFreeMemory

```cpp
static string releaseFreeMemory(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function symbol

```cpp
static string symbol(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800