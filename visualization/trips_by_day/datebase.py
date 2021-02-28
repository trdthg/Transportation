from sqlalchemy import create_engine
import pandas as pd
import pymysql
DB_USER = 'maker0'
DB_PASS = 'Maker0000'
DB_HOST = 'rm-bp11labi01950io698o.mysql.rds.aliyuncs.com'
DB_PORT = 3306
DATABASE = 'library1'
connect_info = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DATABASE)  #1
# 查询语句，选出testexcel表中的所有数据
sql = """select * from trips"""

# read_sql_query的两个参数: sql语句， 数据库连接
df = pd.read_sql_query(sql,con=connect_info)

# 输出testexcel表的查询结果
print(df)