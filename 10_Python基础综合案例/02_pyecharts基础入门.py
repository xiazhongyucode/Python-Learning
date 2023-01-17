"""
演示pyecharts的基础入门
"""
# 导包
from pyecharts.charts import Line
# 创建一个折线图对象
line = Line()
# 给折线图对象添加x轴的数据
line.add_xaxis(["中国","美国","英国"])
# 给折线图对象添加y轴的数据
line.add_yaxis("GDP",[30,20,10])
# 通过render方法，将代码生成为图像
line.render()
# 设置全局配置项