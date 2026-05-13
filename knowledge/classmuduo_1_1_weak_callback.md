---
title: muduo::WeakCallback

---

# muduo::WeakCallback



 [More...](#detailed-description)


`#include <WeakCallback.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[WeakCallback](/classmuduo_1_1_weak_callback.md#function-weakcallback)**(const std::weak_ptr< CLASS > & object, const std::function< void(CLASS *, ARGS...)> & function) |
| void | **[operator()](/classmuduo_1_1_weak_callback.md#function-operator())**(ARGS &&... args) const |

## Detailed Description

```cpp
template <typename CLASS ,
typename... ARGS>
class muduo::WeakCallback;
```

## Public Functions Documentation

### function WeakCallback

```cpp
inline WeakCallback(
    const std::weak_ptr< CLASS > & object,
    const std::function< void(CLASS *, ARGS...)> & function
)
```


### function operator()

```cpp
inline void operator()(
    ARGS &&... args
) const
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800