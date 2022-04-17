# me.py

# 第一种，之前介绍了
import file
print("1", file.create_name())

# 第二种更偷懒
from file import *
print("2", create_name())
print("2", create_time())
