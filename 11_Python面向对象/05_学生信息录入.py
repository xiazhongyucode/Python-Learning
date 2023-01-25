"""
练习：学生信息录入
"""


# 构造类Student
class Student:
    name = None
    age = None
    add = None

    def __init__(self, name, age, add):
        self.name = name
        self.age = age
        self.add = add


# 创建空字典，存放学生信息
stu_dict = {}
# for循环录入信息
for i in range(10):
    print(f"当前录入第{i + 1}位学生信息，总共需要录入10位学生信息。")
    stu = Student(input("请输入学生姓名："), input("请输入学生年龄："), input("请输入学生地址："))
    stu_dict[f"学生{i + 1}"] = {}
    stu_dict[f"学生{i + 1}"]["姓名"] = stu.name
    stu_dict[f"学生{i + 1}"]["年龄"] = stu.age
    stu_dict[f"学生{i + 1}"]["地址"] = stu.add
    print(f"学生{i + 1}信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.add}】")
print("所有学生信息录入完毕。")
print(stu_dict)
