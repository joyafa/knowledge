---
title: muduo

---

# muduo

 [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[muduo::CurrentThread](/namespacemuduo_1_1_current_thread.md)**  |
| **[muduo::detail](/namespacemuduo_1_1detail.md)**  |
| **[muduo::FileUtil](/namespacemuduo_1_1_file_util.md)**  |
| **[muduo::inspect](/namespacemuduo_1_1inspect.md)**  |
| **[muduo::net](/namespacemuduo_1_1net.md)**  |
| **[muduo::ProcessInfo](/namespacemuduo_1_1_process_info.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::AsyncLogging](/classmuduo_1_1_async_logging.md)**  |
| class | **[muduo::BlockingQueue](/classmuduo_1_1_blocking_queue.md)**  |
| class | **[muduo::BoundedBlockingQueue](/classmuduo_1_1_bounded_blocking_queue.md)**  |
| class | **[muduo::Condition](/classmuduo_1_1_condition.md)**  |
| class | **[muduo::copyable](/classmuduo_1_1copyable.md)**  |
| class | **[muduo::CountDownLatch](/classmuduo_1_1_count_down_latch.md)**  |
| class | **[muduo::Date](/classmuduo_1_1_date.md)**  |
| struct | **[muduo::DateTime](/structmuduo_1_1_date_time.md)**  |
| class | **[muduo::Exception](/classmuduo_1_1_exception.md)**  |
| class | **[muduo::Fmt](/classmuduo_1_1_fmt.md)**  |
| class | **[muduo::GzipFile](/classmuduo_1_1_gzip_file.md)**  |
| class | **[muduo::LogFile](/classmuduo_1_1_log_file.md)**  |
| class | **[muduo::Logger](/classmuduo_1_1_logger.md)**  |
| class | **[muduo::LogStream](/classmuduo_1_1_log_stream.md)**  |
| class | **[muduo::MutexLockGuard](/classmuduo_1_1_mutex_lock_guard.md)**  |
| class | **[muduo::noncopyable](/classmuduo_1_1noncopyable.md)**  |
| class | **[muduo::Singleton](/classmuduo_1_1_singleton.md)**  |
| class | **[muduo::StringArg](/classmuduo_1_1_string_arg.md)**  |
| class | **[muduo::StringPiece](/classmuduo_1_1_string_piece.md)**  |
| class | **[muduo::T](/classmuduo_1_1_t.md)**  |
| class | **[muduo::Thread](/classmuduo_1_1_thread.md)**  |
| class | **[muduo::ThreadLocal](/classmuduo_1_1_thread_local.md)**  |
| class | **[muduo::ThreadLocalSingleton](/classmuduo_1_1_thread_local_singleton.md)**  |
| class | **[muduo::ThreadPool](/classmuduo_1_1_thread_pool.md)**  |
| class | **[muduo::Timestamp](/classmuduo_1_1_timestamp.md)**  |
| class | **[muduo::TimeZone](/classmuduo_1_1_time_zone.md)**  |
| class | **[muduo::WeakCallback](/classmuduo_1_1_weak_callback.md)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef [detail::AtomicIntegerT](/classmuduo_1_1detail_1_1_atomic_integer_t.md)< int32_t > | **[AtomicInt32](/namespacemuduo.md#typedef-atomicint32)**  |
| typedef [detail::AtomicIntegerT](/classmuduo_1_1detail_1_1_atomic_integer_t.md)< int64_t > | **[AtomicInt64](/namespacemuduo.md#typedef-atomicint64)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[operator<](/namespacemuduo.md#function-operator<)**([Date](/class_date.md) x, [Date](/class_date.md) y) |
| bool | **[operator==](/namespacemuduo.md#function-operator==)**([Date](/class_date.md) x, [Date](/class_date.md) y) |
| const char * | **[strerror_tl](/namespacemuduo.md#function-strerror-tl)**(int savedErrno) |
| [Logger::LogLevel](/classmuduo_1_1_logger.md#enum-loglevel) | **[initLogLevel](/namespacemuduo.md#function-initloglevel)**() |
| [LogStream](/classmuduo_1_1_log_stream.md) & | **[operator<<](/namespacemuduo.md#function-operator<<)**([LogStream](/classmuduo_1_1_log_stream.md) & s, [T](/classmuduo_1_1_t.md) v) |
| [LogStream](/classmuduo_1_1_log_stream.md) & | **[operator<<](/namespacemuduo.md#function-operator<<)**([LogStream](/classmuduo_1_1_log_stream.md) & s, const [Logger::SourceFile](/classmuduo_1_1_logger_1_1_source_file.md) & v) |
| void | **[defaultOutput](/namespacemuduo.md#function-defaultoutput)**(const char * msg, int len) |
| void | **[defaultFlush](/namespacemuduo.md#function-defaultflush)**() |
| template <typename T \> <br>[T](/classmuduo_1_1_t.md) * | **[CheckNotNull](/namespacemuduo.md#function-checknotnull)**([Logger::SourceFile](/classmuduo_1_1_logger_1_1_source_file.md) file, int line, const char * names, [T](/classmuduo_1_1_t.md) * ptr) |
| std::string | **[formatSI](/namespacemuduo.md#function-formatsi)**(int64_t s) |
| std::string | **[formatIEC](/namespacemuduo.md#function-formatiec)**(int64_t s) |
| [LogStream](/classmuduo_1_1_log_stream.md) & | **[operator<<](/namespacemuduo.md#function-operator<<)**([LogStream](/classmuduo_1_1_log_stream.md) & s, const [Fmt](/classmuduo_1_1_fmt.md) & fmt) |
| bool | **[operator<](/namespacemuduo.md#function-operator<)**([Timestamp](/class_timestamp.md) lhs, [Timestamp](/class_timestamp.md) rhs) |
| bool | **[operator==](/namespacemuduo.md#function-operator==)**([Timestamp](/class_timestamp.md) lhs, [Timestamp](/class_timestamp.md) rhs) |
| double | **[timeDifference](/namespacemuduo.md#function-timedifference)**([Timestamp](/class_timestamp.md) high, [Timestamp](/class_timestamp.md) low) |
| [Timestamp](/class_timestamp.md) | **[addTime](/namespacemuduo.md#function-addtime)**([Timestamp](/class_timestamp.md) timestamp, double seconds) |
| void | **[memZero](/namespacemuduo.md#function-memzero)**(void * p, size_t n) |
| template <typename To ,typename From \> <br>To | **[implicit_cast](/namespacemuduo.md#function-implicit-cast)**(From const & f) |
| template <typename To ,typename From \> <br>To | **[down_cast](/namespacemuduo.md#function-down-cast)**(From * f) |
| template <typename CLASS ,typename... ARGS\> <br>[WeakCallback](/classmuduo_1_1_weak_callback.md)< CLASS, ARGS... > | **[makeWeakCallback](/namespacemuduo.md#function-makeweakcallback)**(const std::shared_ptr< CLASS > & object, void(CLASS::*)(ARGS...) function) |
| template <typename T \> <br>[T](/classmuduo_1_1_t.md) * | **[get_pointer](/namespacemuduo.md#function-get-pointer)**(const std::shared_ptr< [T](/classmuduo_1_1_t.md) > & ptr) |
| template <typename T \> <br>[T](/classmuduo_1_1_t.md) * | **[get_pointer](/namespacemuduo.md#function-get-pointer)**(const std::unique_ptr< [T](/classmuduo_1_1_t.md) > & ptr) |
| template <typename To ,typename From \> <br>inline ::std::shared_ptr< To > | **[down_pointer_cast](/namespacemuduo.md#function-down-pointer-cast)**(const ::std::shared_ptr< From > & f) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| __thread char[512] | **[t_errnobuf](/namespacemuduo.md#variable-t-errnobuf)**  |
| __thread char[64] | **[t_time](/namespacemuduo.md#variable-t-time)**  |
| __thread time_t | **[t_lastSecond](/namespacemuduo.md#variable-t-lastsecond)**  |
| [Logger::LogLevel](/classmuduo_1_1_logger.md#enum-loglevel) | **[g_logLevel](/namespacemuduo.md#variable-g-loglevel)**  |
| const char *[Logger::NUM_LOG_LEVELS] | **[LogLevelName](/namespacemuduo.md#variable-loglevelname)**  |
| [Logger::OutputFunc](/classmuduo_1_1_logger.md#typedef-outputfunc) | **[g_output](/namespacemuduo.md#variable-g-output)**  |
| [Logger::FlushFunc](/classmuduo_1_1_logger.md#typedef-flushfunc) | **[g_flush](/namespacemuduo.md#variable-g-flush)**  |
| [TimeZone](/class_time_zone.md) | **[g_logTimeZone](/namespacemuduo.md#variable-g-logtimezone)**  |
| pthread_once_t | **[Singleton< T >::ponce_](/namespacemuduo.md#variable-singleton<-t->ponce-)**  |
| [T](/classmuduo_1_1_t.md) * | **[Singleton< T >::value_](/namespacemuduo.md#variable-singleton<-t->value-)**  |
| __thread [T](/classmuduo_1_1_t.md) * | **[ThreadLocalSingleton< T >::t_value_](/namespacemuduo.md#variable-threadlocalsingleton<-t->t-value-)**  |
| [ThreadLocalSingleton](/classmuduo_1_1_thread_local_singleton.md)< [T](/classmuduo_1_1_t.md) >::Deleter | **[ThreadLocalSingleton< T >::deleter_](/namespacemuduo.md#variable-threadlocalsingleton<-t->deleter-)**  |
| const int | **[kSecondsPerDay](/namespacemuduo.md#variable-ksecondsperday)**  |

## Detailed Description


The most common stuffs. 

## Types Documentation

### typedef AtomicInt32

```cpp
typedef detail::AtomicIntegerT<int32_t> muduo::AtomicInt32;
```


### typedef AtomicInt64

```cpp
typedef detail::AtomicIntegerT<int64_t> muduo::AtomicInt64;
```



## Functions Documentation

### function operator<

```cpp
inline bool operator<(
    Date x,
    Date y
)
```


### function operator==

```cpp
inline bool operator==(
    Date x,
    Date y
)
```


### function strerror_tl

```cpp
const char * strerror_tl(
    int savedErrno
)
```


### function initLogLevel

```cpp
Logger::LogLevel initLogLevel()
```


### function operator<<

```cpp
inline LogStream & operator<<(
    LogStream & s,
    T v
)
```


### function operator<<

```cpp
inline LogStream & operator<<(
    LogStream & s,
    const Logger::SourceFile & v
)
```


### function defaultOutput

```cpp
void defaultOutput(
    const char * msg,
    int len
)
```


### function defaultFlush

```cpp
void defaultFlush()
```


### function CheckNotNull

```cpp
template <typename T >
T * CheckNotNull(
    Logger::SourceFile file,
    int line,
    const char * names,
    T * ptr
)
```


### function formatSI

```cpp
std::string formatSI(
    int64_t s
)
```


### function formatIEC

```cpp
std::string formatIEC(
    int64_t s
)
```


### function operator<<

```cpp
inline LogStream & operator<<(
    LogStream & s,
    const Fmt & fmt
)
```


### function operator<

```cpp
inline bool operator<(
    Timestamp lhs,
    Timestamp rhs
)
```


### function operator==

```cpp
inline bool operator==(
    Timestamp lhs,
    Timestamp rhs
)
```


### function timeDifference

```cpp
inline double timeDifference(
    Timestamp high,
    Timestamp low
)
```


**Parameters**: 

  * **highlow** 


**Return**: (high-low) in seconds `double` has 52-bit precision, enough for one-microsecond resolution for next 100 years. 

Gets time difference of two timestamps, result in seconds.


### function addTime

```cpp
inline Timestamp addTime(
    Timestamp timestamp,
    double seconds
)
```


**Return**: timestamp+seconds as [Timestamp](/classmuduo_1_1_timestamp.md)

Add `seconds` to given timestamp.


### function memZero

```cpp
inline void memZero(
    void * p,
    size_t n
)
```


### function implicit_cast

```cpp
template <typename To ,
typename From >
inline To implicit_cast(
    From const & f
)
```


### function down_cast

```cpp
template <typename To ,
typename From >
inline To down_cast(
    From * f
)
```


### function makeWeakCallback

```cpp
template <typename CLASS ,
typename... ARGS>
WeakCallback< CLASS, ARGS... > makeWeakCallback(
    const std::shared_ptr< CLASS > & object,
    void(CLASS::*)(ARGS...) function
)
```


### function get_pointer

```cpp
template <typename T >
inline T * get_pointer(
    const std::shared_ptr< T > & ptr
)
```


### function get_pointer

```cpp
template <typename T >
inline T * get_pointer(
    const std::unique_ptr< T > & ptr
)
```


### function down_pointer_cast

```cpp
template <typename To ,
typename From >
inline ::std::shared_ptr< To > down_pointer_cast(
    const ::std::shared_ptr< From > & f
)
```



## Attributes Documentation

### variable t_errnobuf

```cpp
__thread char[512] t_errnobuf;
```


### variable t_time

```cpp
__thread char[64] t_time;
```


### variable t_lastSecond

```cpp
__thread time_t t_lastSecond;
```


### variable g_logLevel

```cpp
Logger::LogLevel g_logLevel = initLogLevel();
```


### variable LogLevelName

```cpp
const char *[Logger::NUM_LOG_LEVELS] LogLevelName                         =
{
  "TRACE ",
  "DEBUG ",
  "INFO  ",
  "WARN  ",
  "ERROR ",
  "FATAL ",
};
```


### variable g_output

```cpp
Logger::OutputFunc g_output = defaultOutput;
```


### variable g_flush

```cpp
Logger::FlushFunc g_flush = defaultFlush;
```


### variable g_logTimeZone

```cpp
TimeZone g_logTimeZone;
```


### variable Singleton< T >::ponce_

```cpp
pthread_once_t Singleton< T >::ponce_ = PTHREAD_ONCE_INIT;
```


### variable Singleton< T >::value_

```cpp
T * Singleton< T >::value_ = NULL;
```


### variable ThreadLocalSingleton< T >::t_value_

```cpp
__thread T * ThreadLocalSingleton< T >::t_value_ = 0;
```


### variable ThreadLocalSingleton< T >::deleter_

```cpp
ThreadLocalSingleton< T >::Deleter ThreadLocalSingleton< T >::deleter_;
```


### variable kSecondsPerDay

```cpp
const int kSecondsPerDay = 24*60*60;
```





-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800