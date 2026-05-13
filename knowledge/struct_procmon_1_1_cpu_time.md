---
title: Procmon::CpuTime

---

# Procmon::CpuTime





## Public Functions

|                | Name           |
| -------------- | -------------- |
| double | **[cpuUsage](/struct_procmon_1_1_cpu_time.md#function-cpuusage)**(double kPeriod, double kClockTicksPerSecond) const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[userTime_](/struct_procmon_1_1_cpu_time.md#variable-usertime-)**  |
| int | **[sysTime_](/struct_procmon_1_1_cpu_time.md#variable-systime-)**  |

## Public Functions Documentation

### function cpuUsage

```cpp
inline double cpuUsage(
    double kPeriod,
    double kClockTicksPerSecond
) const
```


## Public Attributes Documentation

### variable userTime_

```cpp
int userTime_;
```


### variable sysTime_

```cpp
int sysTime_;
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800