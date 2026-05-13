---
title: WordCountSender

---

# WordCountSender





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[WordCountSender](/class_word_count_sender.md#function-wordcountsender)**(const std::string & receivers) |
| void | **[connectAll](/class_word_count_sender.md#function-connectall)**() |
| void | **[disconnectAll](/class_word_count_sender.md#function-disconnectall)**() |
| void | **[processFile](/class_word_count_sender.md#function-processfile)**(const char * filename) |

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

### function WordCountSender

```cpp
explicit WordCountSender(
    const std::string & receivers
)
```


### function connectAll

```cpp
inline void connectAll()
```


### function disconnectAll

```cpp
inline void disconnectAll()
```


### function processFile

```cpp
void processFile(
    const char * filename
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800