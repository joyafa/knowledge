---
title: EventLoop

---

# EventLoop



 [More...](#detailed-description)


`#include <EventLoop.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::function< void()> | **[Functor](/class_event_loop.md#typedef-functor)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[EventLoop](/class_event_loop.md#function-eventloop)**() |
| | **[~EventLoop](/class_event_loop.md#function-~eventloop)**() |
| void | **[loop](/class_event_loop.md#function-loop)**() |
| void | **[quit](/class_event_loop.md#function-quit)**() |
| [Timestamp](/class_timestamp.md) | **[pollReturnTime](/class_event_loop.md#function-pollreturntime)**() const |
| int64_t | **[iteration](/class_event_loop.md#function-iteration)**() const |
| void | **[runInLoop](/class_event_loop.md#function-runinloop)**([Functor](/class_event_loop.md#typedef-functor) cb) |
| void | **[queueInLoop](/class_event_loop.md#function-queueinloop)**([Functor](/class_event_loop.md#typedef-functor) cb) |
| size_t | **[queueSize](/class_event_loop.md#function-queuesize)**() const |
| [TimerId](/classmuduo_1_1net_1_1_timer_id.md) | **[runAt](/class_event_loop.md#function-runat)**([Timestamp](/class_timestamp.md) time, [TimerCallback](/namespacemuduo_1_1net.md#typedef-timercallback) cb) |
| [TimerId](/classmuduo_1_1net_1_1_timer_id.md) | **[runAfter](/class_event_loop.md#function-runafter)**(double delay, [TimerCallback](/namespacemuduo_1_1net.md#typedef-timercallback) cb) |
| [TimerId](/classmuduo_1_1net_1_1_timer_id.md) | **[runEvery](/class_event_loop.md#function-runevery)**(double interval, [TimerCallback](/namespacemuduo_1_1net.md#typedef-timercallback) cb) |
| void | **[cancel](/class_event_loop.md#function-cancel)**([TimerId](/classmuduo_1_1net_1_1_timer_id.md) timerId) |
| void | **[wakeup](/class_event_loop.md#function-wakeup)**() |
| void | **[updateChannel](/class_event_loop.md#function-updatechannel)**([Channel](/classmuduo_1_1net_1_1_channel.md) * channel) |
| void | **[removeChannel](/class_event_loop.md#function-removechannel)**([Channel](/classmuduo_1_1net_1_1_channel.md) * channel) |
| bool | **[hasChannel](/class_event_loop.md#function-haschannel)**([Channel](/classmuduo_1_1net_1_1_channel.md) * channel) |
| void | **[assertInLoopThread](/class_event_loop.md#function-assertinloopthread)**() |
| bool | **[isInLoopThread](/class_event_loop.md#function-isinloopthread)**() const |
| bool | **[eventHandling](/class_event_loop.md#function-eventhandling)**() const |
| void | **[setContext](/class_event_loop.md#function-setcontext)**(const boost::any & context) |
| const boost::any & | **[getContext](/class_event_loop.md#function-getcontext)**() const |
| boost::any * | **[getMutableContext](/class_event_loop.md#function-getmutablecontext)**() |
| [EventLoop](/class_event_loop.md) * | **[getEventLoopOfCurrentThread](/class_event_loop.md#function-geteventloopofcurrentthread)**() |

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
class EventLoop;
```


Reactor, at most one per thread.

This is an interface class, so don't expose too much details. 

## Public Types Documentation

### typedef Functor

```cpp
typedef std::function<void()> muduo::net::EventLoop::Functor;
```


## Public Functions Documentation

### function EventLoop

```cpp
EventLoop()
```


### function ~EventLoop

```cpp
~EventLoop()
```


### function loop

```cpp
void loop()
```


Loops forever.

Must be called in the same thread as creation of the object. 


### function quit

```cpp
void quit()
```


Quits loop.

This is not 100% thread safe, if you call through a raw pointer, better to call through shared_ptr<EventLoop> for 100% safety. 


### function pollReturnTime

```cpp
inline Timestamp pollReturnTime() const
```


Time when poll returns, usually means data arrival. 


### function iteration

```cpp
inline int64_t iteration() const
```


### function runInLoop

```cpp
void runInLoop(
    Functor cb
)
```


Runs callback immediately in the loop thread. It wakes up the loop, and run the cb. If in the same loop thread, cb is run within the function. Safe to call from other threads. 


### function queueInLoop

```cpp
void queueInLoop(
    Functor cb
)
```


Queues callback in the loop thread. Runs after finish pooling. Safe to call from other threads. 


### function queueSize

```cpp
size_t queueSize() const
```


### function runAt

```cpp
TimerId runAt(
    Timestamp time,
    TimerCallback cb
)
```


Runs callback at 'time'. Safe to call from other threads. 


### function runAfter

```cpp
TimerId runAfter(
    double delay,
    TimerCallback cb
)
```


Runs callback after `delay` seconds. Safe to call from other threads. 


### function runEvery

```cpp
TimerId runEvery(
    double interval,
    TimerCallback cb
)
```


Runs callback every `interval` seconds. Safe to call from other threads. 


### function cancel

```cpp
void cancel(
    TimerId timerId
)
```


Cancels the timer. Safe to call from other threads. 


### function wakeup

```cpp
void wakeup()
```


### function updateChannel

```cpp
void updateChannel(
    Channel * channel
)
```


### function removeChannel

```cpp
void removeChannel(
    Channel * channel
)
```


### function hasChannel

```cpp
bool hasChannel(
    Channel * channel
)
```


### function assertInLoopThread

```cpp
inline void assertInLoopThread()
```


### function isInLoopThread

```cpp
inline bool isInLoopThread() const
```


### function eventHandling

```cpp
inline bool eventHandling() const
```


### function setContext

```cpp
inline void setContext(
    const boost::any & context
)
```


### function getContext

```cpp
inline const boost::any & getContext() const
```


### function getMutableContext

```cpp
inline boost::any * getMutableContext()
```


### function getEventLoopOfCurrentThread

```cpp
static EventLoop * getEventLoopOfCurrentThread()
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800