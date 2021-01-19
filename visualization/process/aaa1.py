import pandas  as pd
import numpy as np

# 直接读取

trips = pd.read_csv('./data/trips.csv',encoding='gbk') # 加上header=1能忽略第一行
trips = pd.DataFrame(trips)
print(type(trips['出站时间'][0]))
trips['出站时间'] = pd.to_datetime(trips['出站时间'],format="%Y/%m/%d %H:%M")
trips['进站时间'] = pd.to_datetime(trips['进站时间'],format="%Y/%m/%d %H:%M")
trips = trips.drop(['渠道编号'], axis=1)
year = trips['进站时间'].dt.year
month = trips['进站时间'].dt.month
print(month)

print( trips.loc[ trips['进站时间'].dt.month.isin([2,3,5,6,7]) ]['进站时间'].count())  