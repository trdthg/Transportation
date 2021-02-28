

'''
trips = pd.DataFrame(pd.read_csv('./data/trips.csv',encoding='gbk')) # 加上header=1能忽略第一行
workday = pd.DataFrame(pd.read_csv('./small_workday.csv'))
trips = trips.drop(['渠道编号'], axis=1)
workday = workday.drop(['year'], axis=1)

trips['进站时间'] = pd.to_datetime(trips['进站时间'],format="%Y/%m/%d %H:%M")
trips['inmonth'] = trips['进站时间'].dt.month
trips['inday'] = trips['进站时间'].dt.day

# trips['出站时间'] = pd.to_datetime(trips['出站时间'],format="%Y/%m/%d %H:%M")
# trips['outyear'] = trips['出站时间'].dt.year
# trips['outmonth'] = trips['出站时间'].dt.month
# trips['outday'] = trips['出站时间'].dt.day

trips['dayofweek'] = trips['进站时间'].dt.dayofweek

workday['Column1'] = pd.to_datetime(workday['Column1'], format= "%Y-%m-%d")
workday['month'] =  workday['Column1'].dt.month
workday['day'] =  workday['Column1'].dt.day

trips['dayprop'] = '0'

for index, row in trips.iterrows():
    flag = 0
    for index_, row_ in workday.iterrows():
        if row[6] == row_[2] and row[7]==row_[3]:
            flag = 1
            trips.iloc[index,9] = row_[1]
            print(index)
            break
    if flag == 0:
        trips.iloc[index,9] = 1
trips.to_csv('./new_trips.csv')
# df = trips['inmonth']
# df = pd.DataFrame(df)
# df['inday'] = trips['inday']
# df.to_csv('./small_trips.csv')    
'''

# from sklearn.cluster import SpectralClustering
# import numpy as np
# x1 = [
#     [1, 1], [2, 1], [1, 0],
#     [4, 7], [3, 5], [3, 6]
# ]
# X = np.array([
#     # np.array([1,2,3,4,10,20,56,78,65,66]).reshape(-1,1)
#     # [[1, 1], 
#     #  [1, 2]], 
#     # [[2, 2], 
#     #  [1, 1]], 
#     # [[1, 1], 
#     #  [0, 1]],
#     # [[4, 4], 
#     #  [7, 7]], 
#     # [[3, 3], 
#     #  [5, 5]], 
#     # [[3, 3], 
#     #  [6, 7]]
    
# ]
# )
              
# clustering = SpectralClustering(n_clusters=3,
#         assign_labels="discretize",
#         random_state=0).fit(X)
# print(clustering.labels_)

# print(clustering)


# print('    '[2])

# import csv
# with open('./data/station.csv') as f:
#     f = csv.reader(f)
#     new_dict = {}
#     i = -1
#     for row in f:
#         i+=1
#         if i == 0:
#             continue
#         print(i)
#         new_dict[row[1]] = [row[2], row[4]]
# print(new_dict)

a = {'a':[1,2,3]}
a['a'].append(1)
print(a)


