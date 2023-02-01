"""
演示设计模式之工厂模式
"""


class Person:
    pass


class Worker(Person):
    pass


class Student(Person):
    pass


class Teacher(Person):
    pass


class PersonFactory:
    def getperson(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()


pf = PersonFactory()
worker = pf.getperson('w')
stu = pf.getperson('s')
teacher = pf.getperson('t')
