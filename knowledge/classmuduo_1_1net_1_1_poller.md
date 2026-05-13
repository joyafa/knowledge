---
title: muduo::net::Poller

---

# muduo::net::Poller



 [More...](#detailed-description)


`#include <Poller.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

Inherited by [muduo::net::EPollPoller](/classmuduo_1_1net_1_1_e_poll_poller.md), [muduo::net::PollPoller](/classmuduo_1_1net_1_1_poll_poller.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::vector< [Channel](/classmuduo_1_1net_1_1_channel.md) * > | **[ChannelList](/classmuduo_1_1net_1_1_poller.md#typedef-channellist)**  |

## Protected Types

|                | Name           |
| -------------- | -------------- |
| typedef std::map< int, [Channel](/classmuduo_1_1net_1_1_channel.md) * > | **[ChannelMap](/classmuduo_1_1net_1_1_poller.md#typedef-channelmap)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Poller](/classmuduo_1_1net_1_1_poller.md#function-poller)**([EventLoop](/class_event_loop.md) * loop) |
| virtual | **[~Poller](/classmuduo_1_1net_1_1_poller.md#function-~poller)**() |
| virtual [Timestamp](/class_timestamp.md) | **[poll](/classmuduo_1_1net_1_1_poller.md#function-poll)**(int timeoutMs, [ChannelList](/classmuduo_1_1net_1_1_poller.md#typedef-channellist) * activeChannels) =0 |
| virtual void | **[updateChannel](/classmuduo_1_1net_1_1_poller.md#function-updatechannel)**([Channel](/classmuduo_1_1net_1_1_channel.md) * channel) =0 |
| virtual void | **[removeChannel](/classmuduo_1_1net_1_1_poller.md#function-removechannel)**([Channel](/classmuduo_1_1net_1_1_channel.md) * channel) =0 |
| virtual bool | **[hasChannel](/classmuduo_1_1net_1_1_poller.md#function-haschannel)**([Channel](/classmuduo_1_1net_1_1_channel.md) * channel) const |
| void | **[assertInLoopThread](/classmuduo_1_1net_1_1_poller.md#function-assertinloopthread)**() const |
| [Poller](/classmuduo_1_1net_1_1_poller.md#function-poller) * | **[newDefaultPoller](/classmuduo_1_1net_1_1_poller.md#function-newdefaultpoller)**([EventLoop](/class_event_loop.md) * loop) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| [ChannelMap](/classmuduo_1_1net_1_1_poller.md#typedef-channelmap) | **[channels_](/classmuduo_1_1net_1_1_poller.md#variable-channels-)**  |

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
class muduo::net::Poller;
```


Base class for IO Multiplexing

This class doesn't own the [Channel](/classmuduo_1_1net_1_1_channel.md) objects. 

## Public Types Documentation

### typedef ChannelList

```cpp
typedef std::vector<Channel*> muduo::net::Poller::ChannelList;
```


## Protected Types Documentation

### typedef ChannelMap

```cpp
typedef std::map<int, Channel*> muduo::net::Poller::ChannelMap;
```


## Public Functions Documentation

### function Poller

```cpp
Poller(
    EventLoop * loop
)
```


### function ~Poller

```cpp
virtual ~Poller()
```


### function poll

```cpp
virtual Timestamp poll(
    int timeoutMs,
    ChannelList * activeChannels
) =0
```


**Reimplemented by**: [muduo::net::EPollPoller::poll](/classmuduo_1_1net_1_1_e_poll_poller.md#function-poll), [muduo::net::PollPoller::poll](/classmuduo_1_1net_1_1_poll_poller.md#function-poll)


Polls the I/O events. Must be called in the loop thread. 


### function updateChannel

```cpp
virtual void updateChannel(
    Channel * channel
) =0
```


**Reimplemented by**: [muduo::net::EPollPoller::updateChannel](/classmuduo_1_1net_1_1_e_poll_poller.md#function-updatechannel), [muduo::net::PollPoller::updateChannel](/classmuduo_1_1net_1_1_poll_poller.md#function-updatechannel)


Changes the interested I/O events. Must be called in the loop thread. 


### function removeChannel

```cpp
virtual void removeChannel(
    Channel * channel
) =0
```


**Reimplemented by**: [muduo::net::EPollPoller::removeChannel](/classmuduo_1_1net_1_1_e_poll_poller.md#function-removechannel), [muduo::net::PollPoller::removeChannel](/classmuduo_1_1net_1_1_poll_poller.md#function-removechannel)


Remove the channel, when it destructs. Must be called in the loop thread. 


### function hasChannel

```cpp
virtual bool hasChannel(
    Channel * channel
) const
```


### function assertInLoopThread

```cpp
inline void assertInLoopThread() const
```


### function newDefaultPoller

```cpp
static Poller * newDefaultPoller(
    EventLoop * loop
)
```


## Protected Attributes Documentation

### variable channels_

```cpp
ChannelMap channels_;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800