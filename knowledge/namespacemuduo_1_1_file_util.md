---
title: muduo::FileUtil

---

# muduo::FileUtil



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::FileUtil::ReadSmallFile](/classmuduo_1_1_file_util_1_1_read_small_file.md)**  |
| class | **[muduo::FileUtil::AppendFile](/classmuduo_1_1_file_util_1_1_append_file.md)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| template <typename String \> <br>int | **[readFile](/namespacemuduo_1_1_file_util.md#function-readfile)**([StringArg](/classmuduo_1_1_string_arg.md) filename, int maxSize, String * content, int64_t * fileSize =NULL, int64_t * modifyTime =NULL, int64_t * createTime =NULL) |


## Functions Documentation

### function readFile

```cpp
template <typename String >
int readFile(
    StringArg filename,
    int maxSize,
    String * content,
    int64_t * fileSize =NULL,
    int64_t * modifyTime =NULL,
    int64_t * createTime =NULL
)
```






-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800