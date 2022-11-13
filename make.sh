## 记录了部分常用shell命令
#!/bin/bash
# 数据迁移
python manage.py makemigrations
python manage.py migrate 
# 从数据库里生成model类代码
Python manage.py inspectdb