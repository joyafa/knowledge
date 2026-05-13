---
title: muduo::net::SystemInspector

---

# muduo::net::SystemInspector






`#include <SystemInspector.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[registerCommands](/classmuduo_1_1net_1_1_system_inspector.md#function-registercommands)**([Inspector](/classmuduo_1_1net_1_1_inspector.md) * ins) |
| string | **[overview](/classmuduo_1_1net_1_1_system_inspector.md#function-overview)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[loadavg](/classmuduo_1_1net_1_1_system_inspector.md#function-loadavg)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[version](/classmuduo_1_1net_1_1_system_inspector.md#function-version)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[cpuinfo](/classmuduo_1_1net_1_1_system_inspector.md#function-cpuinfo)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[meminfo](/classmuduo_1_1net_1_1_system_inspector.md#function-meminfo)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[stat](/classmuduo_1_1net_1_1_system_inspector.md#function-stat)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |

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


### function overview

```cpp
static string overview(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function loadavg

```cpp
static string loadavg(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function version

```cpp
static string version(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function cpuinfo

```cpp
static string cpuinfo(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function meminfo

```cpp
static string meminfo(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function stat

```cpp
static string stat(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800