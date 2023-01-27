"""
SQL综合案例，读取文件，写入MySql数据库中
"""
from pymysql import Connection
from data_define import Record
from file_define import TextFileReader, JsonFileReader

text_file_reader = TextFileReader("2011年1月销售数据.txt")
json_file_reader = JsonFileReader("2011年2月销售数据JSON.txt")
jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
# 将2个月份的数据合并为1个list来存储
all_data: list[Record] = jan_data + feb_data
# print(all_data)
# 构建MySql链接对象
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="Xzy200825",
    autocommit=True
)
# 获得游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("py_sql")
# 组织SQL语句
for record in all_data:
    sql = f"insert into orders(order_date,order_id,money,province)" \
          f"values('{record.date}','{record.order_id}',{record.money},'{record.province}')"
    # 执行SQL语句
    cursor.execute(sql)
# 关闭MySql链接对象
conn.close()