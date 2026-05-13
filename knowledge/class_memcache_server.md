---
title: MemcacheServer

---

# MemcacheServer






`#include <MemcacheServer.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Options](/struct_memcache_server_1_1_options.md)**  |
| struct | **[Stats](/struct_memcache_server_1_1_stats.md)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[MemcacheServer](/class_memcache_server.md#function-memcacheserver)**([muduo::net::EventLoop](/classmuduo_1_1net_1_1_event_loop.md) * loop, const [Options](/struct_options.md) & options) |
| | **[~MemcacheServer](/class_memcache_server.md#function-~memcacheserver)**() |
| void | **[setThreadNum](/class_memcache_server.md#function-setthreadnum)**(int threads) |
| void | **[start](/class_memcache_server.md#function-start)**() |
| void | **[stop](/class_memcache_server.md#function-stop)**() |
| time_t | **[startTime](/class_memcache_server.md#function-starttime)**() const |
| bool | **[storeItem](/class_memcache_server.md#function-storeitem)**(const [ItemPtr](/_item_8h.md#typedef-itemptr) & item, [Item::UpdatePolicy](/class_item.md#enum-updatepolicy) policy, bool * exists) |
| [ConstItemPtr](/_item_8h.md#typedef-constitemptr) | **[getItem](/class_memcache_server.md#function-getitem)**(const [ConstItemPtr](/_item_8h.md#typedef-constitemptr) & key) const |
| bool | **[deleteItem](/class_memcache_server.md#function-deleteitem)**(const [ConstItemPtr](/_item_8h.md#typedef-constitemptr) & key) |

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

### function MemcacheServer

```cpp
MemcacheServer(
    muduo::net::EventLoop * loop,
    const Options & options
)
```


### function ~MemcacheServer

```cpp
~MemcacheServer()
```


### function setThreadNum

```cpp
inline void setThreadNum(
    int threads
)
```


### function start

```cpp
void start()
```


### function stop

```cpp
void stop()
```


### function startTime

```cpp
inline time_t startTime() const
```


### function storeItem

```cpp
bool storeItem(
    const ItemPtr & item,
    Item::UpdatePolicy policy,
    bool * exists
)
```


### function getItem

```cpp
ConstItemPtr getItem(
    const ConstItemPtr & key
) const
```


### function deleteItem

```cpp
bool deleteItem(
    const ConstItemPtr & key
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800