---
title: examples/wordcount/hash.h

---

# examples/wordcount/hash.h



## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::unordered_map< muduo::string, int64_t > | **[WordCountMap](/hash_8h.md#typedef-wordcountmap)**  |

## Types Documentation

### typedef WordCountMap

```cpp
typedef std::unordered_map<muduo::string, int64_t> WordCountMap;
```





## Source code

```cpp
#ifndef MUDUO_EXAMPLES_WORDCOUNT_HASH_H
#define MUDUO_EXAMPLES_WORDCOUNT_HASH_H

#include <unordered_map>

typedef std::unordered_map<muduo::string, int64_t> WordCountMap;

#endif  // MUDUO_EXAMPLES_WORDCOUNT_HASH_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
