"""
演示Python正则表达式使用元字符进行匹配
"""
import re

# s = "itheima @@python2 !!666 ##itcast3"
#
# result = re.findall(r'[a-zA-Z]', s)  # 字符串前面带上r的标记，表示字符串中转义字符串无效，就是普通字符的意思
# print(result)

# 匹配账号，只能由字母和数字组成，长度限制6到10位
# r = '^[0-9a-zA-Z]{6,10}$'
# s = '123456_'
# print(re.findall(r, s))
# 匹配QQ号，要求纯数字，长度5-11，第一位不为0
# r = '^[1-9][0-9]{4,10}$'
# s = '12345678'
# print(re.findall(r, s))
# 匹配邮箱地址，只允许qq、163、gmail这三种邮箱地址
# abc.efg.daw@qq.com
# abc@qq.com
# {内容}.{内容}.{内容}.{内容}.{内容}.{内容}@{内容}.{内容}.{内容}
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]+)+$)'
# s = 'a.c.d.e.f.g@qq.com.a.z.c.d.e'
s = 'a.c.d.e.f.g@162.com.a.z.c.d.e'
print(re.match(r, s))
