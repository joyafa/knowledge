---
title: examples/ace/ttcp/main.cc

---

# examples/ace/ttcp/main.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| int | **[main](/ace_2ttcp_2main_8cc.md#function-main)**(int argc, char * argv[]) |


## Functions Documentation

### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```




## Source code

```cpp
#include "examples/ace/ttcp/common.h"

#include <assert.h>

int main(int argc, char* argv[])
{
  Options options;
  if (parseCommandLine(argc, argv, &options))
  {
    if (options.transmit)
    {
      transmit(options);
    }
    else if (options.receive)
    {
      receive(options);
    }
    else
    {
      assert(0);
    }
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
