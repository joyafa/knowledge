---
title: muduo::net::Inspector

---

# muduo::net::Inspector






`#include <Inspector.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::vector< string > | **[ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist)**  |
| typedef std::function< string([HttpRequest::Method](/classmuduo_1_1net_1_1_http_request.md#enum-method), const [ArgList](/classmuduo_1_1net_1_1_inspector.md#typedef-arglist) &args)> | **[Callback](/classmuduo_1_1net_1_1_inspector.md#typedef-callback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Inspector](/classmuduo_1_1net_1_1_inspector.md#function-inspector)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & httpAddr, const string & name) |
| | **[~Inspector](/classmuduo_1_1net_1_1_inspector.md#function-~inspector)**() |
| void | **[add](/classmuduo_1_1net_1_1_inspector.md#function-add)**(const string & module, const string & command, const [Callback](/classmuduo_1_1net_1_1_inspector.md#typedef-callback) & cb, const string & help)<br>Add a [Callback](/class_callback.md) for handling the special uri : /mudule/command.  |
| void | **[remove](/classmuduo_1_1net_1_1_inspector.md#function-remove)**(const string & module, const string & command) |

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

### typedef ArgList

```cpp
typedef std::vector<string> muduo::net::Inspector::ArgList;
```


### typedef Callback

```cpp
typedef std::function<string (HttpRequest::Method, const ArgList& args)> muduo::net::Inspector::Callback;
```


## Public Functions Documentation

### function Inspector

```cpp
Inspector(
    EventLoop * loop,
    const InetAddress & httpAddr,
    const string & name
)
```


### function ~Inspector

```cpp
~Inspector()
```


### function add

```cpp
void add(
    const string & module,
    const string & command,
    const Callback & cb,
    const string & help
)
```

Add a [Callback](/class_callback.md) for handling the special uri : /mudule/command. 

### function remove

```cpp
void remove(
    const string & module,
    const string & command
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800