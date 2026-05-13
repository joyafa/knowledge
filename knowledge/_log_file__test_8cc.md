---
title: muduo/base/tests/LogFile_test.cc

---

# muduo/base/tests/LogFile_test.cc



## Functions

|                | Name           |
| -------------- | -------------- |
| void | **[outputFunc](/_log_file__test_8cc.md#function-outputfunc)**(const char * msg, int len) |
| void | **[flushFunc](/_log_file__test_8cc.md#function-flushfunc)**() |
| int | **[main](/_log_file__test_8cc.md#function-main)**(int argc, char * argv[]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| std::unique_ptr< [muduo::LogFile](/classmuduo_1_1_log_file.md) > | **[g_logFile](/_log_file__test_8cc.md#variable-g-logfile)**  |


## Functions Documentation

### function outputFunc

```cpp
void outputFunc(
    const char * msg,
    int len
)
```


### function flushFunc

```cpp
void flushFunc()
```


### function main

```cpp
int main(
    int argc,
    char * argv[]
)
```



## Attributes Documentation

### variable g_logFile

```cpp
std::unique_ptr< muduo::LogFile > g_logFile;
```



## Source code

```cpp
#include "muduo/base/LogFile.h"
#include "muduo/base/Logging.h"

#include <unistd.h>

std::unique_ptr<muduo::LogFile> g_logFile;

void outputFunc(const char* msg, int len)
{
  g_logFile->append(msg, len);
}

void flushFunc()
{
  g_logFile->flush();
}

int main(int argc, char* argv[])
{
  char name[256] = { '\0' };
  strncpy(name, argv[0], sizeof name - 1);
  g_logFile.reset(new muduo::LogFile(::basename(name), 200*1000));
  muduo::Logger::setOutput(outputFunc);
  muduo::Logger::setFlush(flushFunc);

  muduo::string line = "1234567890 abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ ";

  for (int i = 0; i < 10000; ++i)
  {
    LOG_INFO << line << i;

    usleep(1000);
  }
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
