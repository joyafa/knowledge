---
title: muduo::net::Channel

---

# muduo::net::Channel



 [More...](#detailed-description)


`#include <Channel.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void()> | **[EventCallback](/classmuduo_1_1net_1_1_channel.md#typedef-eventcallback)**  |
| typedef std::function< void([Timestamp](/class_timestamp.md))> | **[ReadEventCallback](/classmuduo_1_1net_1_1_channel.md#typedef-readeventcallback)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Channel](/classmuduo_1_1net_1_1_channel.md#function-channel)**([EventLoop](/class_event_loop.md) * loop, int fd) |
| | **[~Channel](/classmuduo_1_1net_1_1_channel.md#function-~channel)**() |
| void | **[handleEvent](/classmuduo_1_1net_1_1_channel.md#function-handleevent)**([Timestamp](/class_timestamp.md) receiveTime) |
| void | **[setReadCallback](/classmuduo_1_1net_1_1_channel.md#function-setreadcallback)**([ReadEventCallback](/classmuduo_1_1net_1_1_channel.md#typedef-readeventcallback) cb) |
| void | **[setWriteCallback](/classmuduo_1_1net_1_1_channel.md#function-setwritecallback)**([EventCallback](/classmuduo_1_1net_1_1_channel.md#typedef-eventcallback) cb) |
| void | **[setCloseCallback](/classmuduo_1_1net_1_1_channel.md#function-setclosecallback)**([EventCallback](/classmuduo_1_1net_1_1_channel.md#typedef-eventcallback) cb) |
| void | **[setErrorCallback](/classmuduo_1_1net_1_1_channel.md#function-seterrorcallback)**([EventCallback](/classmuduo_1_1net_1_1_channel.md#typedef-eventcallback) cb) |
| void | **[tie](/classmuduo_1_1net_1_1_channel.md#function-tie)**(const std::shared_ptr< void > & obj) |
| int | **[fd](/classmuduo_1_1net_1_1_channel.md#function-fd)**() const |
| int | **[events](/classmuduo_1_1net_1_1_channel.md#function-events)**() const |
| void | **[set_revents](/classmuduo_1_1net_1_1_channel.md#function-set-revents)**(int revt) |
| bool | **[isNoneEvent](/classmuduo_1_1net_1_1_channel.md#function-isnoneevent)**() const |
| void | **[enableReading](/classmuduo_1_1net_1_1_channel.md#function-enablereading)**() |
| void | **[disableReading](/classmuduo_1_1net_1_1_channel.md#function-disablereading)**() |
| void | **[enableWriting](/classmuduo_1_1net_1_1_channel.md#function-enablewriting)**() |
| void | **[disableWriting](/classmuduo_1_1net_1_1_channel.md#function-disablewriting)**() |
| void | **[disableAll](/classmuduo_1_1net_1_1_channel.md#function-disableall)**() |
| bool | **[isWriting](/classmuduo_1_1net_1_1_channel.md#function-iswriting)**() const |
| bool | **[isReading](/classmuduo_1_1net_1_1_channel.md#function-isreading)**() const |
| int | **[index](/classmuduo_1_1net_1_1_channel.md#function-index)**() |
| void | **[set_index](/classmuduo_1_1net_1_1_channel.md#function-set-index)**(int idx) |
| string | **[reventsToString](/classmuduo_1_1net_1_1_channel.md#function-reventstostring)**() const |
| string | **[eventsToString](/classmuduo_1_1net_1_1_channel.md#function-eventstostring)**() const |
| void | **[doNotLogHup](/classmuduo_1_1net_1_1_channel.md#function-donotloghup)**() |
| [EventLoop](/class_event_loop.md) * | **[ownerLoop](/classmuduo_1_1net_1_1_channel.md#function-ownerloop)**() |
| void | **[remove](/classmuduo_1_1net_1_1_channel.md#function-remove)**() |

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


## Detailed Description

```cpp
class muduo::net::Channel;
```


A selectable I/O channel.

This class doesn't own the file descriptor. The file descriptor could be a socket, an eventfd, a timerfd, or a signalfd 

## Public Types Documentation

### typedef EventCallback

```cpp
typedef std::function<void()> muduo::net::Channel::EventCallback;
```


### typedef ReadEventCallback

```cpp
typedef std::function<void(Timestamp)> muduo::net::Channel::ReadEventCallback;
```


## Public Functions Documentation

### function Channel

```cpp
Channel(
    EventLoop * loop,
    int fd
)
```


### function ~Channel

```cpp
~Channel()
```


### function handleEvent

```cpp
void handleEvent(
    Timestamp receiveTime
)
```


### function setReadCallback

```cpp
inline void setReadCallback(
    ReadEventCallback cb
)
```


### function setWriteCallback

```cpp
inline void setWriteCallback(
    EventCallback cb
)
```


### function setCloseCallback

```cpp
inline void setCloseCallback(
    EventCallback cb
)
```


### function setErrorCallback

```cpp
inline void setErrorCallback(
    EventCallback cb
)
```


### function tie

```cpp
void tie(
    const std::shared_ptr< void > & obj
)
```


Tie this channel to the owner object managed by shared_ptr, prevent the owner object being destroyed in handleEvent. 


### function fd

```cpp
inline int fd() const
```


### function events

```cpp
inline int events() const
```


### function set_revents

```cpp
inline void set_revents(
    int revt
)
```


### function isNoneEvent

```cpp
inline bool isNoneEvent() const
```


### function enableReading

```cpp
inline void enableReading()
```


### function disableReading

```cpp
inline void disableReading()
```


### function enableWriting

```cpp
inline void enableWriting()
```


### function disableWriting

```cpp
inline void disableWriting()
```


### function disableAll

```cpp
inline void disableAll()
```


### function isWriting

```cpp
inline bool isWriting() const
```


### function isReading

```cpp
inline bool isReading() const
```


### function index

```cpp
inline int index()
```


### function set_index

```cpp
inline void set_index(
    int idx
)
```


### function reventsToString

```cpp
string reventsToString() const
```


### function eventsToString

```cpp
string eventsToString() const
```


### function doNotLogHup

```cpp
inline void doNotLogHup()
```


### function ownerLoop

```cpp
inline EventLoop * ownerLoop()
```


### function remove

```cpp
void remove()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800