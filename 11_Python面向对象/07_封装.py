"""
演示面向对象封装思想中私有成员的使用
"""


# 定义一个类，内含私有成员变量和私有成员方法
class Phone:
    __current_voltage = None  # 当前手机运行电压

    def __keep_single_core(self):
        print("让CPU以单核模式运行")


phone = Phone()
# phone.__keep_single_core()
# print(phone.__current_voltage)
