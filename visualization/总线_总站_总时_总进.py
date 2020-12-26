import xlrd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import multiprocessing as mp

routes_stations = {}
def main():
    print('正在获取文件')
    book_station = xlrd.open_workbook('dataFolder/station.xlsx')
    book_trips = xlrd.open_workbook('dataFolder/trips.xlsx')
    print('正在获取表格')
    sheet_station = book_station.sheets()[0]
    sheet_trips = book_trips.sheets()[0]
    print('正在解析表格')
    col_datalist_station_station = sheet_station.col_values(1,start_rowx=1,end_rowx=None)
    col_datalist_station_route = sheet_station.col_values(2,start_rowx=1,end_rowx=None)
    col_datalist_trips_arrival = sheet_trips.col_values(3,start_rowx=1,end_rowx=None)

    allstations = mp.Manager().dict()

    # routes_stations = {}
    # allstations = set()
    print('开始统计')
    getdatalist(routes_stations, col_datalist_station_route, col_datalist_station_station, allstations)

    print('多核遍历中')
    pool = mp.Pool(12)
    for arrival in col_datalist_trips_arrival:
        pool.apply_async(gettrip, (arrival, allstations))   #维持执行的进程总数为processes，当一个进程执行完毕后会添加新的进程进去
    pool.close()
    pool.join()   #调用join之前，先调用close函数，否则会出错。执行完close后不会有新的进程加入到pool,join函数等待所有子进程结束
    print ("Sub-process(es) done.")

    # for arrival in col_datalist_trips_arrival:
    #     allstations[arrival] += 1
    print (allstations)

    drawpicture_one(allstations)
    # drawpicture_many(lines)
    
    
def gettrip(arrival,allstations):
    # global allstations
    print(arrival)
    allstations[arrival] += 1

def getstations(router,col_datalist_station_station,col_datalist_station_route, allstations):
    # global allstations
    for station, route in zip(col_datalist_station_station,col_datalist_station_route):
        routes_stations[route].add(station)
        if station not in allstations.keys():
            allstations[station] = 0

def getdatalist(routes_stations, col_datalist_station_route, col_datalist_station_station, allstations):
    # global allstations
    for route in set(col_datalist_station_route):
        routes_stations[route] = set()
    print('得到了所有的线路')
    print(routes_stations.keys())
    for route in routes_stations.keys():
        print(f'正在获取{route}的车站')
        getstations(route,col_datalist_station_station,col_datalist_station_route, allstations)
        print(routes_stations[route])


def drawpicture_many(lines):
        # 单图展示
        for line in lines:
            plt.figure()
            n = len(line)
            x = line.keys()
            y = line.values()
            ax = plt.gca()
            for label in ax.get_xticklabels():
                label.set_fontsize(10)
            plt.plot(x,y)
            # break
        print('开始绘图')
        plt.show()

def drawpicture_one(allstations):
        fig = plt.figure(figsize=(20,40))
        # fig.set_figheight(300)
        # fig.set_figwidth(100)
        i=0
        k=0
        j=0
        for route in routes_stations.keys():
            ax = plt.subplot2grid( ( int(len(routes_stations.keys())/2.0)+1 , 2), (i,k), rowspan=1, colspan=1)
            x = routes_stations[route]  # x为关于线路上站点的列表
            y = []
            for station in x:
                y.append(allstations[station])
            ax.plot(list(x), list(y))
            ax.set_title(routes_stations.keys(), fontproperties="FangSong")
            j += 1
            i += 1
            if k==0: 
                k=1
                i-=5
            else: k=0
        plt.tight_layout(w_pad=5, h_pad=15)
        # plt.subplots_adjust(hspace =20)#调整子图间距
        print('开始绘图')
        plt.show()

if __name__ == '__main__':
    main()

