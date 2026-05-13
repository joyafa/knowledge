# 用户服务 API

## 功能概述

用户服务提供用户注册、登录、信息查询、权限管理等功能。所有接口基于 RESTful 风格设计，基础路径为 `/api/v1/users`。

## 认证方式

所有接口（除注册和登录外）需要在请求头中携带 JWT Token：

```
Authorization: Bearer <token>
```

Token 有效期为 2 小时，过期后需要重新登录获取。

---

## 注册接口

### POST /api/v1/users/register

注册新用户账号。

**参数说明：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| username | string | 是 | 用户名，3-20 个字符，仅支持字母数字下划线 |
| password | string | 是 | 密码，8-32 个字符，需包含大小写字母和数字 |
| email | string | 是 | 邮箱地址，用于接收验证邮件 |
| phone | string | 否 | 手机号，格式为 11 位数字 |

**请求示例：**

```python
import requests

response = requests.post("http://api.example.com/api/v1/users/register", json={
    "username": "zhangsan",
    "password": "MyPass123",
    "email": "zhangsan@example.com",
    "phone": "13800138000"
})

print(response.json())
# {"code": 0, "message": "注册成功", "data": {"user_id": 10042}}
```

**返回值：**

| 字段 | 类型 | 说明 |
|------|------|------|
| code | int | 状态码，0 表示成功 |
| message | string | 提示信息 |
| data.user_id | int | 新创建的用户 ID |

**错误码：**

| code | 说明 |
|------|------|
| 1001 | 用户名已存在 |
| 1002 | 邮箱已被注册 |
| 1003 | 参数格式不合法 |

---

## 登录接口

### POST /api/v1/users/login

用户登录获取 Token。

**参数说明：**

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| username | string | 是 | 用户名 |
| password | string | 是 | 密码 |

**请求示例：**

```python
response = requests.post("http://api.example.com/api/v1/users/login", json={
    "username": "zhangsan",
    "password": "MyPass123"
})

print(response.json())
# {"code": 0, "data": {"token": "eyJhbGciOiJIUzI1NiIs...", "expires_in": 7200}}
```

**错误码：**

| code | 说明 |
|------|------|
| 2001 | 用户名或密码错误 |
| 2002 | 账号已被锁定（连续 5 次密码错误） |

---

## 查询用户信息

### GET /api/v1/users/{user_id}

查询指定用户的详细信息。需要登录 Token。

**路径参数：**

| 参数名 | 类型 | 说明 |
|--------|------|------|
| user_id | int | 用户 ID |

**请求示例：**

```python
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIs..."}
response = requests.get("http://api.example.com/api/v1/users/10042", headers=headers)

print(response.json())
# {
#   "code": 0,
#   "data": {
#     "user_id": 10042,
#     "username": "zhangsan",
#     "email": "zhangsan@example.com",
#     "role": "developer",
#     "created_at": "2026-01-15T10:30:00Z"
#   }
# }
```

**错误码：**

| code | 说明 |
|------|------|
| 3001 | 用户不存在 |
| 3002 | 无权限查看该用户信息 |
