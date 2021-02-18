import pandas  as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import calendar
from collections import Counter
import shortestpass
# trips = pd.DataFrame(pd.read_csv('./data/trips.csv',encoding='gbk')) # 加上header=1能忽略第一行
# workday = pd.DataFrame(pd.read_csv('./small_workday.csv'))
# trips = trips.drop(['渠道编号'], axis=1)
# workday = workday.drop(['year'], axis=1)

# trips['进站时间'] = pd.to_datetime(trips['进站时间'],format="%Y/%m/%d %H:%M")
# trips['inmonth'] = trips['进站时间'].dt.month
# trips['inday'] = trips['进站时间'].dt.day

# # trips['出站时间'] = pd.to_datetime(trips['出站时间'],format="%Y/%m/%d %H:%M")
# # trips['outyear'] = trips['出站时间'].dt.year
# # trips['outmonth'] = trips['出站时间'].dt.month
# # trips['outday'] = trips['出站时间'].dt.day

# trips['dayofweek'] = trips['进站时间'].dt.dayofweek

# workday['Column1'] = pd.to_datetime(workday['Column1'], format= "%Y-%m-%d")
# workday['month'] =  workday['Column1'].dt.month
# workday['day'] =  workday['Column1'].dt.day

# trips['dayprop'] = '0'

# for index, row in trips.iterrows():
#     flag = 0
#     for index_, row_ in workday.iterrows():
#         if row[6] == row_[2] and row[7]==row_[3]:
#             flag = 1
#             trips.iloc[index,9] = row_[1]
#             print(index)
#             break
#     if flag == 0:
#         trips.iloc[index,9] = 1
# trips.to_csv('./new_trips.csv')
# # df = trips['inmonth']
# # df = pd.DataFrame(df)
# # df['inday'] = trips['inday']
# # df.to_csv('./small_trips.csv')    


trips = pd.DataFrame(pd.read_csv('./data/new_trips.csv'))
stations = pd.DataFrame(pd.read_csv('./data/station.csv', encoding='gbk'))

year = 2020
flow = {}  
for month in [1,2,3,4,5,6,7,8,12]:
    flow[month] = {}
    # 获取该月的所有trips数据
    res = calendar.monthrange(year,month)
    df = pd.DataFrame(trips.loc[trips['inmonth'] == month])
    for day in range(1, res[1]):
        # 获取该天的所有trips数据
        df_day = df.loc[df['inday'] == day]
        df_day = df_day.loc[df_day['hour']==7]
        print(month ,'-' , day)

        list1,list2,list3,list4 = [],[],[],[]
        temp = {

        }
        
        for index, row in df_day.iterrows():
            # 统计啥
            # 根据输入时间给出
            # 全网站点和路径的客流(level)
            # 加入A~B花费时间的推算

            # 1. 站点 进站/出站 流量
            # 2. 线路客流
            # 3. 换乘客流
            
            # 1.
            stain, staout = row[2], row[4]
            if stain in temp.keys():
                temp[stain][0] += 1
            else:
                temp[stain] = [1, 0]
            if staout in temp.keys():
                temp[staout][1] += 1
            else:
                temp[stain] = [0, 1]
            # 2.







            shortestpass.main(stain, staout)
        for key in temp.keys():
            list1.append({'station':key,'in':temp[key][0], 'out':temp[key][1]})


        print()
        break
        # print(df_day)
        # df_day.to_csv(f'./day_trips/{month}-{day}.csv')   
    break

# rows = []

# headers = ['month', 'day', 'sta', 'flow']
# with open('./route_flow_by_day.csv','w',newline='', encoding='utf-8') as f2:
#     f2_csv = csv.writer(f2)
#     f2_csv.writerow(headers)
#     f2_csv.writerows(rows)

