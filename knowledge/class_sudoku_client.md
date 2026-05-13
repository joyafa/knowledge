---
title: SudokuClient

---

# SudokuClient





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md), [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SudokuClient](/class_sudoku_client.md#function-sudokuclient)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr, const [InputPtr](/pipeline_8cc.md#typedef-inputptr) & input, const string & name, const [DoneCallback](/batch_8cc.md#typedef-donecallback) & cb) |
| void | **[connect](/class_sudoku_client.md#function-connect)**() |
| | **[SudokuClient](/class_sudoku_client.md#function-sudokuclient)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr, const [InputPtr](/pipeline_8cc.md#typedef-inputptr) & input, const string & name, bool nodelay) |
| void | **[connect](/class_sudoku_client.md#function-connect)**() |
| void | **[send](/class_sudoku_client.md#function-send)**(int n) |
| void | **[report](/class_sudoku_client.md#function-report)**(std::vector< int > * latency, int * infly) |
| | **[SudokuClient](/class_sudoku_client.md#function-sudokuclient)**([EventLoop](/class_event_loop.md) * loop, const [InetAddress](/class_inet_address.md) & serverAddr, const [InputPtr](/pipeline_8cc.md#typedef-inputptr) & input, const string & name, int pipelines, bool nodelay) |
| void | **[connect](/class_sudoku_client.md#function-connect)**() |
| void | **[report](/class_sudoku_client.md#function-report)**(std::vector< int > * latency, int * infly) |

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

### function SudokuClient

```cpp
inline SudokuClient(
    EventLoop * loop,
    const InetAddress & serverAddr,
    const InputPtr & input,
    const string & name,
    const DoneCallback & cb
)
```


### function connect

```cpp
inline void connect()
```


### function SudokuClient

```cpp
inline SudokuClient(
    EventLoop * loop,
    const InetAddress & serverAddr,
    const InputPtr & input,
    const string & name,
    bool nodelay
)
```


### function connect

```cpp
inline void connect()
```


### function send

```cpp
inline void send(
    int n
)
```


### function report

```cpp
inline void report(
    std::vector< int > * latency,
    int * infly
)
```


### function SudokuClient

```cpp
inline SudokuClient(
    EventLoop * loop,
    const InetAddress & serverAddr,
    const InputPtr & input,
    const string & name,
    int pipelines,
    bool nodelay
)
```


### function connect

```cpp
inline void connect()
```


### function report

```cpp
inline void report(
    std::vector< int > * latency,
    int * infly
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800