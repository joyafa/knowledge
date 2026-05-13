---
title: examples/ace/ttcp/common.h

---

# examples/ace/ttcp/common.h



## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Options](/struct_options.md)**  |
| struct | **[SessionMessage](/struct_session_message.md)**  |
| struct | **[PayloadMessage](/struct_payload_message.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| bool | **[parseCommandLine](/common_8h.md#function-parsecommandline)**(int argc, char * argv[], [Options](/struct_options.md) * opt) |
| struct sockaddr_in | **[resolveOrDie](/common_8h.md#function-resolveordie)**(const char * host, uint16_t port) |
| struct [SessionMessage](/struct_session_message.md) | **[__attribute__](/common_8h.md#function---attribute--)**((__packed__) ) |
| void | **[transmit](/common_8h.md#function-transmit)**(const [Options](/struct_options.md) & opt) |
| void | **[receive](/common_8h.md#function-receive)**(const [Options](/struct_options.md) & opt) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| int32_t | **[number](/common_8h.md#variable-number)**  |
| int32_t | **[length](/common_8h.md#variable-length)**  |
| struct [PayloadMessage](/struct_payload_message.md) | **[__attribute__](/common_8h.md#variable---attribute--)**  |


## Functions Documentation

### function parseCommandLine

```cpp
bool parseCommandLine(
    int argc,
    char * argv[],
    Options * opt
)
```


### function resolveOrDie

```cpp
struct sockaddr_in resolveOrDie(
    const char * host,
    uint16_t port
)
```


### function __attribute__

```cpp
struct SessionMessage __attribute__(
    (__packed__) 
)
```


### function transmit

```cpp
void transmit(
    const Options & opt
)
```


### function receive

```cpp
void receive(
    const Options & opt
)
```



## Attributes Documentation

### variable number

```cpp
int32_t number;
```


### variable length

```cpp
int32_t length;
```


### variable __attribute__

```cpp
struct PayloadMessage __attribute__;
```



## Source code

```cpp
#pragma once

#include <string>
#include <stdint.h>

struct Options
{
  uint16_t port;
  int length;
  int number;
  bool transmit, receive, nodelay;
  std::string host;
  Options()
    : port(0), length(0), number(0),
      transmit(false), receive(false), nodelay(false)
  {
  }
};

bool parseCommandLine(int argc, char* argv[], Options* opt);
struct sockaddr_in resolveOrDie(const char* host, uint16_t port);

struct SessionMessage
{
  int32_t number;
  int32_t length;
} __attribute__ ((__packed__));

struct PayloadMessage
{
  int32_t length;
  char data[0];
};

void transmit(const Options& opt);

void receive(const Options& opt);
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
