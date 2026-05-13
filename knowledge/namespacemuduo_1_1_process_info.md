---
title: muduo::ProcessInfo

---

# muduo::ProcessInfo



## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[muduo::ProcessInfo::CpuTime](/structmuduo_1_1_process_info_1_1_cpu_time.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| pid_t | **[pid](/namespacemuduo_1_1_process_info.md#function-pid)**() |
| string | **[pidString](/namespacemuduo_1_1_process_info.md#function-pidstring)**() |
| uid_t | **[uid](/namespacemuduo_1_1_process_info.md#function-uid)**() |
| string | **[username](/namespacemuduo_1_1_process_info.md#function-username)**() |
| uid_t | **[euid](/namespacemuduo_1_1_process_info.md#function-euid)**() |
| [Timestamp](/class_timestamp.md) | **[startTime](/namespacemuduo_1_1_process_info.md#function-starttime)**() |
| int | **[clockTicksPerSecond](/namespacemuduo_1_1_process_info.md#function-clocktickspersecond)**() |
| int | **[pageSize](/namespacemuduo_1_1_process_info.md#function-pagesize)**() |
| bool | **[isDebugBuild](/namespacemuduo_1_1_process_info.md#function-isdebugbuild)**() |
| string | **[hostname](/namespacemuduo_1_1_process_info.md#function-hostname)**() |
| string | **[procname](/namespacemuduo_1_1_process_info.md#function-procname)**() |
| [StringPiece](/classmuduo_1_1_string_piece.md) | **[procname](/namespacemuduo_1_1_process_info.md#function-procname)**(const string & stat) |
| string | **[procStatus](/namespacemuduo_1_1_process_info.md#function-procstatus)**()<br>read /proc/self/status  |
| string | **[procStat](/namespacemuduo_1_1_process_info.md#function-procstat)**()<br>read /proc/self/stat  |
| string | **[threadStat](/namespacemuduo_1_1_process_info.md#function-threadstat)**()<br>read /proc/self/task/tid/stat  |
| string | **[exePath](/namespacemuduo_1_1_process_info.md#function-exepath)**()<br>readlink /proc/self/exe  |
| int | **[openedFiles](/namespacemuduo_1_1_process_info.md#function-openedfiles)**() |
| int | **[maxOpenFiles](/namespacemuduo_1_1_process_info.md#function-maxopenfiles)**() |
| [CpuTime](/structmuduo_1_1_process_info_1_1_cpu_time.md) | **[cpuTime](/namespacemuduo_1_1_process_info.md#function-cputime)**() |
| int | **[numThreads](/namespacemuduo_1_1_process_info.md#function-numthreads)**() |
| std::vector< pid_t > | **[threads](/namespacemuduo_1_1_process_info.md#function-threads)**() |


## Functions Documentation

### function pid

```cpp
pid_t pid()
```


### function pidString

```cpp
string pidString()
```


### function uid

```cpp
uid_t uid()
```


### function username

```cpp
string username()
```


### function euid

```cpp
uid_t euid()
```


### function startTime

```cpp
Timestamp startTime()
```


### function clockTicksPerSecond

```cpp
int clockTicksPerSecond()
```


### function pageSize

```cpp
int pageSize()
```


### function isDebugBuild

```cpp
bool isDebugBuild()
```


### function hostname

```cpp
string hostname()
```


### function procname

```cpp
string procname()
```


### function procname

```cpp
StringPiece procname(
    const string & stat
)
```


### function procStatus

```cpp
string procStatus()
```

read /proc/self/status 

### function procStat

```cpp
string procStat()
```

read /proc/self/stat 

### function threadStat

```cpp
string threadStat()
```

read /proc/self/task/tid/stat 

### function exePath

```cpp
string exePath()
```

readlink /proc/self/exe 

### function openedFiles

```cpp
int openedFiles()
```


### function maxOpenFiles

```cpp
int maxOpenFiles()
```


### function cpuTime

```cpp
CpuTime cpuTime()
```


### function numThreads

```cpp
int numThreads()
```


### function threads

```cpp
std::vector< pid_t > threads()
```






-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800