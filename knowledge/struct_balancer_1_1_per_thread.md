---
title: Balancer::PerThread

---

# Balancer::PerThread





## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[PerThread](/struct_balancer_1_1_per_thread.md#function-perthread)**() |
| | **[PerThread](/struct_balancer_1_1_per_thread.md#function-perthread)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| size_t | **[current](/struct_balancer_1_1_per_thread.md#variable-current)**  |
| std::vector< std::unique_ptr< [BackendSession](/class_backend_session.md) > > | **[backends](/struct_balancer_1_1_per_thread.md#variable-backends)**  |

## Public Functions Documentation

### function PerThread

```cpp
inline PerThread()
```


### function PerThread

```cpp
inline PerThread()
```


## Public Attributes Documentation

### variable current

```cpp
size_t current;
```


### variable backends

```cpp
std::vector< std::unique_ptr< BackendSession > > backends;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800