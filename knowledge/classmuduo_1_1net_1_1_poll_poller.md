---
title: muduo::net::PollPoller

---

# muduo::net::PollPoller



 [More...](#detailed-description)


`#include <PollPoller.h>`

Inherits from [muduo::net::Poller](/classmuduo_1_1net_1_1_poller.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[PollPoller](/classmuduo_1_1net_1_1_poll_poller.md#function-pollpoller)**([EventLoop](/class_event_loop.md) * loop) |
| | **[~PollPoller](/classmuduo_1_1net_1_1_poll_poller.md#function-~pollpoller)**() override |
| virtual [Timestamp](/class_timestamp.md) | **[poll](/classmuduo_1_1net_1_1_poll_poller.md#function-poll)**(int timeoutMs, [ChannelList](/classmuduo_1_1net_1_1_poller.md#typedef-channellist) * activeChannels) override |
| virtual void | **[updateChannel](/classmuduo_1_1net_1_1_poll_poller.md#function-updatechannel)**([Channel](/classmuduo_1_1net_1_1_channel.md) * channel) override |
| virtual void | **[removeChannel](/classmuduo_1_1net_1_1_poll_poller.md#function-removechannel)**([Channel](/classmuduo_1_1net_1_1_channel.md) * channel) override |

## Additional inherited members

**Public Types inherited from [muduo::net::Poller](/classmuduo_1_1net_1_1_poller.md)**

|                | Name           |
| -------------- | -------------- |
| typedef std::vector< [Channel](/classmuduo_1_1net_1_1_channel.md) * > | **[ChannelList](/classmuduo_1_1net_1_1_poller.md#typedef-channellist)**  |

**Protected Types inherited from [muduo::net::Poller](/classmuduo_1_1net_1_1_poller.md)**

|                | Name           |
| -------------- | -------------- |
| typedef std::map< int, [Channel](/classmuduo_1_1net_1_1_channel.md) * > | **[ChannelMap](/classmuduo_1_1net_1_1_poller.md#typedef-channelmap)**  |

**Public Functions inherited from [muduo::net::Poller](/classmuduo_1_1net_1_1_poller.md)**

|                | Name           |
| -------------- | -------------- |
| | **[Poller](/classmuduo_1_1net_1_1_poller.md#function-poller)**([EventLoop](/class_event_loop.md) * loop) |
| virtual | **[~Poller](/classmuduo_1_1net_1_1_poller.md#function-~poller)**() |
| virtual bool | **[hasChannel](/classmuduo_1_1net_1_1_poller.md#function-haschannel)**([Channel](/classmuduo_1_1net_1_1_channel.md) * channel) const |
| void | **[assertInLoopThread](/classmuduo_1_1net_1_1_poller.md#function-assertinloopthread)**() const |
| [Poller](/classmuduo_1_1net_1_1_poller.md#function-poller) * | **[newDefaultPoller](/classmuduo_1_1net_1_1_poller.md#function-newdefaultpoller)**([EventLoop](/class_event_loop.md) * loop) |

**Protected Attributes inherited from [muduo::net::Poller](/classmuduo_1_1net_1_1_poller.md)**

|                | Name           |
| -------------- | -------------- |
| [ChannelMap](/classmuduo_1_1net_1_1_poller.md#typedef-channelmap) | **[channels_](/classmuduo_1_1net_1_1_poller.md#variable-channels-)**  |

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
class muduo::net::PollPoller;
```


IO Multiplexing with poll(2). 

## Public Functions Documentation

### function PollPoller

```cpp
PollPoller(
    EventLoop * loop
)
```


### function ~PollPoller

```cpp
~PollPoller() override
```


### function poll

```cpp
virtual Timestamp poll(
    int timeoutMs,
    ChannelList * activeChannels
) override
```


**Reimplements**: [muduo::net::Poller::poll](/classmuduo_1_1net_1_1_poller.md#function-poll)


Polls the I/O events. Must be called in the loop thread. 


### function updateChannel

```cpp
virtual void updateChannel(
    Channel * channel
) override
```


**Reimplements**: [muduo::net::Poller::updateChannel](/classmuduo_1_1net_1_1_poller.md#function-updatechannel)


Changes the interested I/O events. Must be called in the loop thread. 


### function removeChannel

```cpp
virtual void removeChannel(
    Channel * channel
) override
```


**Reimplements**: [muduo::net::Poller::removeChannel](/classmuduo_1_1net_1_1_poller.md#function-removechannel)


Remove the channel, when it destructs. Must be called in the loop thread. 


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800