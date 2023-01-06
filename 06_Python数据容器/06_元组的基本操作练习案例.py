"""
定义一个元组，内容是：('周杰伦',11,['football','music'])，记录的是一个学生的信息(姓名、年龄、爱好)
请通过元组的功能(方法)，对其进行
1.查询其年龄所在的下标位置
2.查询学生的姓名
3.删除学生爱好中的football
4.增加爱好：coding到爱好list内
"""
student = ('周杰伦', 11, ['football', 'music'])

index = student.index(11)
print(f"其年龄所在的下标位置为：{index}")

print(f"学生的姓名为：{student[0]}")

del student[2][0]
print(f"该元组为:{student}")

student[2].append('coding')
print(f"该元组为:{student}")
