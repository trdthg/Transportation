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

col_datalist_trips_station = sheet_trips.col_values(1,start_rowx=1,end_rowx=None)
col_datalist_trips_arrival = sheet_trips.col_values(2,start_rowx=1,end_rowx=None)
col_datalist_trips_departure = sheet_trips.col_values(4,start_rowx=1,end_rowx=None)

def main():
    datalist = getdatalist()

    # drawpicture_one(datalist[0], datalist[1])
    # drawpicture_many(lines)
    plt.show()

def Statistics(router):
        # 传入的是路线route
        # -----------------------------------------------------
        #    优化条目汇总
        # 🕊 这里可以使用多进程优化
        # 🕊 这里按三行分别获取不太好, 可以换思路,尝试按行遍历
        # -----------------------------------------------------

        # 得到该线路的所有站点
        stations = set()
        for route, station in zip(col_datalist_station_route, col_datalist_station_station):
            if route == router:
                stations.add(station)
        stations = list(stations)
        month_arrival = {'1':0, '2':0, '3':'0', '4':0}
        for station in stations:
            for trip_station, trip_arrival, trip_departure in zip(col_datalist_trips_station, col_datalist_trips_arrival, col_datalist_trips_departure):
                if trip_station == router:
                    
def getdatalist():
    # routes = []
    # for route in col_datalist_station_route:
    #     if route not in routes:
    #         routes.append(route)
    routes = list(set(col_datalist_station_route))
    print(routes)
    lines = []
    for route in routes:
        lines.append(Statistics(route))
    return [lines,routes]

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

def drawpicture_one(lines,routes):
        fig = plt.figure(figsize=(20,40))
        # fig.set_figheight(300)
        # fig.set_figwidth(100)
        i=0
        k=0
        j=0
        for line in lines:
            
            ax = plt.subplot2grid((int(len(routes)/2),2), (i,k), rowspan=1, colspan=1)
            x = line.keys()
            y = line.values()
            ax.plot(x, y)
            ax.set_title(routes[j], fontproperties="FangSong")
            j += 1
            i += 1
            if k==0: 
                k=1
                i-=1
            else: k=0
        plt.tight_layout(w_pad=10, h_pad=20)
        # plt.subplots_adjust(hspace =20)#调整子图间距

if __name__ == '__main__':
    main()

