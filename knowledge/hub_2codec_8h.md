---
title: examples/hub/codec.h

---

# examples/hub/codec.h



## Namespaces

| Name           |
| -------------- |
| **[pubsub](/namespacepubsub.md)**  |




## Source code

```cpp
#ifndef MUDUO_EXAMPLES_HUB_CODEC_H
#define MUDUO_EXAMPLES_HUB_CODEC_H

// internal header file

#include "muduo/base/Types.h"
#include "muduo/net/Buffer.h"

namespace pubsub
{
using muduo::string;

enum ParseResult
{
  kError,
  kSuccess,
  kContinue,
};

ParseResult parseMessage(muduo::net::Buffer* buf,
                         string* cmd,
                         string* topic,
                         string* content);
}  // namespace pubsub

#endif  // MUDUO_EXAMPLES_HUB_CODEC_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
