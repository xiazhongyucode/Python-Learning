"""
演示可视化需求1：折线图开发
"""
import json

# 处理数据
f_us = open("折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()  # 美国的全部内容
# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
# 去掉不合JSON规范的结尾
us_data = us_data[:-2]
# JSON转Python字典
us_dict = json.loads(us_data)

# 获取trend key
trend_data = us_dict['data'][0]['trend']
# print(type(trend_data))
# print(trend_data)
# 获取日期数据，用于x轴，取2020年（到316下标结束）
x_data = trend_data['updateDate'][:314]
print(x_data)
# 获取确认数据，用于y轴，取2020年（到315下标结束）
y_data = trend_data['list'][0]['data']
print(y_data)
# 生成图表
