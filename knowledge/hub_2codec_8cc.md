---
title: examples/hub/codec.cc

---

# examples/hub/codec.cc






## Source code

```cpp
#include "examples/hub/codec.h"

using namespace muduo;
using namespace muduo::net;
using namespace pubsub;

ParseResult pubsub::parseMessage(Buffer* buf,
                                 string* cmd,
                                 string* topic,
                                 string* content)
{
  ParseResult result = kError;
  const char* crlf = buf->findCRLF();
  if (crlf)
  {
    const char* space = std::find(buf->peek(), crlf, ' ');
    if (space != crlf)
    {
      cmd->assign(buf->peek(), space);
      topic->assign(space+1, crlf);
      if (*cmd == "pub")
      {
        const char* start = crlf + 2;
        crlf = buf->findCRLF(start);
        if (crlf)
        {
          content->assign(start, crlf);
          buf->retrieveUntil(crlf+2);
          result = kSuccess;
        }
        else
        {
          result = kContinue;
        }
      }
      else
      {
        buf->retrieveUntil(crlf+2);
        result = kSuccess;
      }
    }
    else
    {
      result = kError;
    }
  }
  else
  {
    result = kContinue;
  }
  return result;
}
```


-------------------------------

Updated on 2026-05-11 at 23:17:10 +0800
