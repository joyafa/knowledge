---
title: muduo/base/Date.h

---

# muduo/base/Date.h



## Namespaces

| Name           |
| -------------- |
| **[muduo](/namespacemuduo.md)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[muduo::Date](/classmuduo_1_1_date.md)**  |
| struct | **[muduo::Date::YearMonthDay](/structmuduo_1_1_date_1_1_year_month_day.md)**  |




## Source code

```cpp
// Use of this source code is governed by a BSD-style license
// that can be found in the License file.
//
// Author: Shuo Chen (chenshuo at chenshuo dot com)

#ifndef MUDUO_BASE_DATE_H
#define MUDUO_BASE_DATE_H

#include "muduo/base/copyable.h"
#include "muduo/base/Types.h"

struct tm;

namespace muduo
{

class Date : public muduo::copyable
          // public boost::less_than_comparable<Date>,
          // public boost::equality_comparable<Date>
{
 public:

  struct YearMonthDay
  {
    int year; // [1900..2500]
    int month;  // [1..12]
    int day;  // [1..31]
  };

  static const int kDaysPerWeek = 7;
  static const int kJulianDayOf1970_01_01;

  Date()
    : julianDayNumber_(0)
  {}

  Date(int year, int month, int day);

  explicit Date(int julianDayNum)
    : julianDayNumber_(julianDayNum)
  {}

  explicit Date(const struct tm&);

  // default copy/assignment/dtor are Okay

  void swap(Date& that)
  {
    std::swap(julianDayNumber_, that.julianDayNumber_);
  }

  bool valid() const { return julianDayNumber_ > 0; }

  string toIsoString() const;

  struct YearMonthDay yearMonthDay() const;

  int year() const
  {
    return yearMonthDay().year;
  }

  int month() const
  {
    return yearMonthDay().month;
  }

  int day() const
  {
    return yearMonthDay().day;
  }

  // [0, 1, ..., 6] => [Sunday, Monday, ..., Saturday ]
  int weekDay() const
  {
    return (julianDayNumber_+1) % kDaysPerWeek;
  }

  int julianDayNumber() const { return julianDayNumber_; }

 private:
  int julianDayNumber_;
};

inline bool operator<(Date x, Date y)
{
  return x.julianDayNumber() < y.julianDayNumber();
}

inline bool operator==(Date x, Date y)
{
  return x.julianDayNumber() == y.julianDayNumber();
}

}  // namespace muduo

#endif  // MUDUO_BASE_DATE_H
```


-------------------------------

Updated on 2026-05-11 at 23:17:11 +0800
