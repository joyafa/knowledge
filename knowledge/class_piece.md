---
title: Piece

---

# Piece





Inherits from [muduo::noncopyable](/classmuduo_1_1noncopyable.md)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Piece](/class_piece.md#function-piece)**(const [curl::RequestPtr](/namespacecurl.md#typedef-requestptr) & req, const [FilePtr](/curl_2download_8cc.md#typedef-fileptr) & out, const muduo::string & range, std::function< void()> done) |

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


## Public Functions Documentation

### function Piece

```cpp
inline Piece(
    const curl::RequestPtr & req,
    const FilePtr & out,
    const muduo::string & range,
    std::function< void()> done
)
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800