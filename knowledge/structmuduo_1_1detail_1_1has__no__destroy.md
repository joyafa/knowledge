---
title: muduo::detail::has_no_destroy

---

# muduo::detail::has_no_destroy



 [More...](#detailed-description)


`#include <Singleton.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| template <typename C \> <br>char | **[test](/structmuduo_1_1detail_1_1has__no__destroy.md#function-test)**(decltype &::no_destroy ) |
| template <typename C \> <br>int32_t | **[test](/structmuduo_1_1detail_1_1has__no__destroy.md#function-test)**(... ) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const bool | **[value](/structmuduo_1_1detail_1_1has__no__destroy.md#variable-value)**  |

## Detailed Description

```cpp
template <typename T >
struct muduo::detail::has_no_destroy;
```

## Public Functions Documentation

### function test

```cpp
template <typename C >
static char test(
    decltype &::no_destroy 
)
```


### function test

```cpp
template <typename C >
static int32_t test(
    ... 
)
```


## Public Attributes Documentation

### variable value

```cpp
static const bool value = sizeof(test<T>(0)) == 1;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800