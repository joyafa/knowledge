---
title: muduo::net::ProcessInspector

---

# muduo::net::ProcessInspector






`#include <ProcessInspector.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| void | **[registerCommands](/classmuduo_1_1net_1_1_process_inspector.md#function-registercommands)**([Inspector](/classmuduo_1_1net_1_1_inspector.md) * ins) |
| string | **[overview](/classmuduo_1_1net_1_1_process_inspector.md#function-overview)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[pid](/classmuduo_1_1net_1_1_process_inspector.md#function-pid)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[procStatus](/classmuduo_1_1net_1_1_process_inspector.md#function-procstatus)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[openedFiles](/classmuduo_1_1net_1_1_process_inspector.md#function-openedfiles)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |
| string | **[threads](/classmuduo_1_1net_1_1_process_inspector.md#function-threads)**([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method) , const [Inspector::ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) & ) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| string | **[username_](/classmuduo_1_1net_1_1_process_inspector.md#variable-username-)**  |

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


### function pid

```cpp
static string pid(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function procStatus

```cpp
static string procStatus(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function openedFiles

```cpp
static string openedFiles(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


### function threads

```cpp
static string threads(
    HttpRequest::Method ,
    const Inspector::ArgList & 
)
```


## Public Attributes Documentation

### variable username_

```cpp
static string username_ = ProcessInfo::username();
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800