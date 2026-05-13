---
title: Procmon

---

# Procmon





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Procmon](/class_procmon.md#function-procmon)**([EventLoop](/class_event_loop.md) * loop, pid_t pid, uint16_t port, const char * procname) |
| void | **[start](/class_procmon.md#function-start)**() |

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

### function Procmon

```cpp
inline Procmon(
    EventLoop * loop,
    pid_t pid,
    uint16_t port,
    const char * procname
)
```


### function start

```cpp
inline void start()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800