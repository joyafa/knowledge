# C++ 函数 API 说明文档示例

## 函数名称
`bool IsPrime(int number)`

## 简介
判断传入的整数是否为质数。

## 参数
- `number`：待检测的整数。

## 返回值
- `true`：`number` 是质数。
- `false`：`number` 不是质数，或 `number <= 1`。

## 详细说明
本函数用于判断 32 位有符号整数是否为质数。质数定义为大于 1 且仅能被 1 和自身整除的正整数。

### 注意事项
- 对于 `number <= 1`，函数返回 `false`。
- 该函数不处理负数质数概念，`number < 2` 时统一返回 `false`。

## 使用示例
```cpp
#include <iostream>

bool IsPrime(int number);

int main() {
    int value = 17;
    if (IsPrime(value)) {
        std::cout << value << " 是质数\n";
    } else {
        std::cout << value << " 不是质数\n";
    }
    return 0;
}
```

## 备注
- 这是一个简单的 API 文档示例，适合作为向量库知识库中的文档条目。
- 你可以根据项目需求，补充更多函数列表、异常处理和性能说明。