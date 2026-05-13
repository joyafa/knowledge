---
title: WordCountReceiver

---

# WordCountReceiver





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[WordCountReceiver](/class_word_count_receiver.md#function-wordcountreceiver)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & listenAddr) |
| void | **[start](/class_word_count_receiver.md#function-start)**(int senders) |

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

### function WordCountReceiver

```cpp
inline WordCountReceiver(
    EventLoop * loop,
    const InetAddress & listenAddr
)
```


### function start

```cpp
inline void start(
    int senders
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800