---
title: muduo::CountDownLatch

---

# muduo::CountDownLatch






`#include <CountDownLatch.h>`

Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[CountDownLatch](/classmuduo_1_1_count_down_latch.md#function-countdownlatch)**(int count) |
| void | **[wait](/classmuduo_1_1_count_down_latch.md#function-wait)**() |
| void | **[countDown](/classmuduo_1_1_count_down_latch.md#function-countdown)**() |
| int | **[getCount](/classmuduo_1_1_count_down_latch.md#function-getcount)**() const |

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

### function CountDownLatch

```cpp
explicit CountDownLatch(
    int count
)
```


### function wait

```cpp
void wait()
```


### function countDown

```cpp
void countDown()
```


### function getCount

```cpp
int getCount() const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800