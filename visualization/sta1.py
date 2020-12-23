import xlrd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec

book_station = xlrd.open_workbook('dataFolder/station.xls')
book_trips = xlrd.open_workbook('dataFolder/trips.xls')
sheet_station = book_station.sheets()[0]
sheet_trips = book_trips.sheets()[0]

col_datalist_station_station = sheet_station.col_values(1,start_rowx=1,end_rowx=None)
col_datalist_station_route = sheet_station.col_values(2,start_rowx=1,end_rowx=None)

def Statistics(router):
    line = {}
    # 添加1号线的站点 
    for station, route in zip(col_datalist_station_station,col_datalist_station_route):
        if route == router:
            if station not in line.keys():
                line[station] = 0
            # else: 
            #     line[station] += 1
    # 计算1号线各个站点的总入站量
    col_datalist_trips_arrival = sheet_trips.col_values(1,start_rowx=1,end_rowx=None)
    for arrival in col_datalist_trips_arrival:
        if arrival in line:
            line[arrival] += 1
    # for key, value in line.items():
    #     print(f'{key}:{value}')
    # print(line)
    return line
# 画图
routes = []
for route in col_datalist_station_route:
    if route not in routes:
        routes.append(route)
print(routes)
lines = []
for route in routes:
    lines.append(Statistics(route))

# 单图展示
# for line in lines:
#     plt.figure()
#     n = len(line)
#     x = line.keys()
#     y = line.values()
#     ax = plt.gca()
#     for label in ax.get_xticklabels():
#         label.set_fontsize(10)
#     plt.plot(x,y)
    # break

fig = plt.figure(figsize=(20,40))
# fig.set_figheight(300)
# fig.set_figwidth(100)
i=0
k=0
for line in lines:
    
    ax = plt.subplot2grid((int(len(routes)/2),2), (i,k), rowspan=1, colspan=1)
    x = line.keys()
    y = line.values()
    ax.plot(x, y)
    ax.set_title(routes[i], fontproperties="FangSong")
    i += 1
    if k==0: 
        k=1
        i-=1
    else: k=0
plt.tight_layout(w_pad=10, h_pad=20)
# plt.subplots_adjust(hspace =20)#调整子图间距

plt.show()


