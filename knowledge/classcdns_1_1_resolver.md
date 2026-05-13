---
title: cdns::Resolver

---

# cdns::Resolver






`#include <Resolver.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| enum| **[Option](/classcdns_1_1_resolver.md#enum-option)** { kDNSandHostsFile, kDNSonly} |
| typedef std::function< void(const [muduo::net::InetAddress](/classmuduo_1_1net_1_1_inet_address.md) &)> | **[Callback](/classcdns_1_1_resolver.md#typedef-callback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Resolver](/classcdns_1_1_resolver.md#function-resolver)**([muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * loop, [Option](/classcdns_1_1_resolver.md#enum-option) opt =[kDNSandHostsFile](/classcdns_1_1_resolver.md#enumvalue-kdnsandhostsfile)) |
| | **[~Resolver](/classcdns_1_1_resolver.md#function-~resolver)**() |
| bool | **[resolve](/classcdns_1_1_resolver.md#function-resolve)**([muduo::StringArg](/classmuduo_1_1_string_arg.md) hostname, const [Callback](/classcdns_1_1_resolver.md#typedef-callback) & cb) |

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
| kDNSandHostsFile | |   |
| kDNSonly | |   |




### typedef Callback

```cpp
typedef std::function<void(const muduo::net::InetAddress&)> cdns::Resolver::Callback;
```


## Public Functions Documentation

### function Resolver

```cpp
explicit Resolver(
    muduo::net::EventLoop * loop,
    Option opt =kDNSandHostsFile
)
```


### function ~Resolver

```cpp
~Resolver()
```


### function resolve

```cpp
bool resolve(
    muduo::StringArg hostname,
    const Callback & cb
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800