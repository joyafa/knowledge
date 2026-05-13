---
title: muduo::CurrentThread

---

# muduo::CurrentThread



## Functions

|                | Name           |
| -------------- | -------------- |
| string | **[stackTrace](/namespacemuduo_1_1_current_thread.md#function-stacktrace)**(bool demangle) |
| void | **[cacheTid](/namespacemuduo_1_1_current_thread.md#function-cachetid)**() |
| int | **[tid](/namespacemuduo_1_1_current_thread.md#function-tid)**() |
| const char * | **[tidString](/namespacemuduo_1_1_current_thread.md#function-tidstring)**() |
| int | **[tidStringLength](/namespacemuduo_1_1_current_thread.md#function-tidstringlength)**() |
| const char * | **[name](/namespacemuduo_1_1_current_thread.md#function-name)**() |
| bool | **[isMainThread](/namespacemuduo_1_1_current_thread.md#function-ismainthread)**() |
| void | **[sleepUsec](/namespacemuduo_1_1_current_thread.md#function-sleepusec)**(int64_t usec) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| __thread int | **[t_cachedTid](/namespacemuduo_1_1_current_thread.md#variable-t-cachedtid)**  |
| __thread char[32] | **[t_tidString](/namespacemuduo_1_1_current_thread.md#variable-t-tidstring)**  |
| __thread int | **[t_tidStringLength](/namespacemuduo_1_1_current_thread.md#variable-t-tidstringlength)**  |
| __thread const char * | **[t_threadName](/namespacemuduo_1_1_current_thread.md#variable-t-threadname)**  |


## Functions Documentation

### function stackTrace

```cpp
string stackTrace(
    bool demangle
)
```


### function cacheTid

```cpp
void cacheTid()
```


### function tid

```cpp
inline int tid()
```


### function tidString

```cpp
inline const char * tidString()
```


### function tidStringLength

```cpp
inline int tidStringLength()
```


### function name

```cpp
inline const char * name()
```


### function isMainThread

```cpp
bool isMainThread()
```


### function sleepUsec

```cpp
void sleepUsec(
    int64_t usec
)
```



## Attributes Documentation

### variable t_cachedTid

```cpp
__thread int t_cachedTid = 0;
```


### variable t_tidString

```cpp
__thread char[32] t_tidString;
```


### variable t_tidStringLength

```cpp
__thread int t_tidStringLength = 6;
```


### variable t_threadName

```cpp
__thread const char * t_threadName = "unknown";
```





-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800