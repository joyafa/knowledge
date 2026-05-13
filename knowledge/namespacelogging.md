---
title: logging

---

# logging



## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[logging::LogClient](/classlogging_1_1_log_client.md)**  |
| class | **[logging::LogServer](/classlogging_1_1_log_server.md)**  |
| class | **[logging::Session](/classlogging_1_1_session.md)**  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef [ProtobufCodecLiteT](/classmuduo_1_1net_1_1_protobuf_codec_lite_t.md)< LogRecord, [logtag](/namespacelogging.md#variable-logtag) > | **[Codec](/namespacelogging.md#typedef-codec)**  |
| typedef std::shared_ptr< [Session](/class_session.md) > | **[SessionPtr](/namespacelogging.md#typedef-sessionptr)**  |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const char[] | **[logtag](/namespacelogging.md#variable-logtag)**  |

## Types Documentation

### typedef Codec

```cpp
typedef ProtobufCodecLiteT< LogRecord, logtag > logging::Codec;
```


### typedef SessionPtr

```cpp
typedef std::shared_ptr<Session> logging::SessionPtr;
```




## Attributes Documentation

### variable logtag

```cpp
const char[] logtag = "LOG0";
```





-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800