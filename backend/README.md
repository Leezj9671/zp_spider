# 后端接口

用于提供数据搜索结果的接口，以及用户注册登陆的接口。

## 语言及模块

1. 语言
- Python 3.6

2. 模块：
- flask-restful
- flask_sqlalchemy

## 运行方式

```bash
python3 run.py
```

## API示例
API|说明
--|--
/api/jobs?page=[int] | 获取当前所有招聘信息的第N页
/api/jobs/[string]?page=[int] | 获取指定关键字招聘信息的第N页

## TODO
1. 