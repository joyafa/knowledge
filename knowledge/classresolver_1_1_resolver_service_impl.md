---
title: resolver::ResolverServiceImpl

---

# resolver::ResolverServiceImpl





Inherits from ResolverService

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ResolverServiceImpl](/classresolver_1_1_resolver_service_impl.md#function-resolverserviceimpl)**([EventLoop](/class_event_loop.md) * loop) |
| virtual void | **[Resolve](/classresolver_1_1_resolver_service_impl.md#function-resolve)**(::google::protobuf::RpcController * controller, const ::resolver::ResolveRequest * request, ::resolver::ResolveResponse * response, ::google::protobuf::Closure * done) |

## Public Functions Documentation

### function ResolverServiceImpl

```cpp
inline ResolverServiceImpl(
    EventLoop * loop
)
```


### function Resolve

```cpp
inline virtual void Resolve(
    ::google::protobuf::RpcController * controller,
    const ::resolver::ResolveRequest * request,
    ::resolver::ResolveResponse * response,
    ::google::protobuf::Closure * done
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800