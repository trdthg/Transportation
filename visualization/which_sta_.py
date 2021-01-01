import csv

def getstations():
    # ['编号', '站点名称', '线路', '行政区域']
    with open('./dataFolder/station.csv') as f:
        f = csv.reader(f)
        routes = {}
        i = 0
        for row in f:
            if i==0:
                i+=1
                continue
            if row[2] not in routes.keys():
                routes[row[2]] = []
            if row[1] not in routes[row[2]]:
                routes[row[2]].append(row[1])
    return routes

stationdatalist = getstations()
print(stationdatalist.keys())
def jjj(j, arr, route):
    # print(j)
    flag = 0
    if j >= len(stationdatalist[route])*2-2:
        pass
    else:
        with open('./dataFolder/a_b_same.csv') as f1:
            f1 = csv.reader(f1)
            for row_ in f1:
                if row_[1]==route and row_[4]==route:
                    stain, staout, time = row_[0], row_[3], row_[6]
                    if arr[j] == stain:
                        if staout not in arr:
                            # print(stain, staout)
                            arr.append(time)
                            arr.append(staout)
                            j += 2
                            flag = 1
                            break
                    elif arr[j] == staout:
                        if stain not in arr:
                            arr.append(time)
                            arr.append(stain)  
                            j += 2
                            flag = 1
                            break
            
        jjj(j, arr, route)
for route in getstations().keys():
    with open('./dataFolder/a_b_same.csv') as f:
        f = csv.reader(f)
        i = 0
        arr = [0,0,0]
        for row in f:
            if i==0:
                i+=1
                continue
            if row[1]==route and row[4]==route:
                i+=1
                arr[0] = row[0]
                arr[1] = row[6]
                arr[2] = row[3]
                # print (arr)
                jjj(2, arr, route)
                break
            # ['Sta64', '1号线', 'Dist3', 'Sta150', '1号线', 'Dist3', '3']
            i+=1
    # print(arr[-1])
    with open('./dataFolder/a_b_same.csv') as f:
        f = csv.reader(f)
        for row in f:
            if (row[0]==arr[-1] and row[3]==arr[0]) or (row[0]==arr[0] and row[3]==arr[-1]):
                arr.append(row[6])
                break

    print (route,arr)
    # break



