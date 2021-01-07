sdict = {'origin':{
            'before':{
                'a11':{
                    'a111':{
                    },
                    },
                'a12':{
                    'a121':{
                        'a1211':{
                        },
                        },
                        },
                        },
            'after':{
                'b11':{
                    'b21':{
                    },
                    },
                    },
                    },
        'sss':{}}
def sss(child_dict):
    for key in child_dict.keys():
        print(key)
        child_dict_ = child_dict[key]
        if child_dict_ == {}:
            # 到达尽头
            continue
        else:
            # 深入到下一层
            sss(child_dict_)
# for key in sdict.keys():
#     print (key)
#     child_dict = sdict[key]
#     # 子字典自我遍历
#     for key in child_dict.keys():
#         print(key)
#         child_dict_ = child_dict[key]
#         if child_dict_ == {}:
#             # 到达尽头
#             continue
#         else:
#             # 深入到下一层
#             sss(child_dict_)
# flag = 0
# sss(sdict)
p = ['lll','kkk','iiii','ooo']
# print(p.index('kkk'))
import csv
a = ['Sta77', '4', 'Sta122', '5', 'Sta36', '16', 'Sta28', '3', 'Sta124', '7', 'Sta166', '3', 'Sta99', '30', 'Sta45', '10', 'Sta152', '5', 'Sta164', '5', 'Sta82', '4', 'Sta111', '4', 'Sta140', '6', 'Sta13', '4', 'Sta70', '3', 'Sta55', '4', 'Sta20', '3', 'Sta23', '3', 'Sta56', '4', 'Sta118', '4', 'Sta115', '3', 'Sta162', '6', 'Sta15', '4', 'Sta86', '3', 'Sta46', '3', 'Sta63', '3', 'Sta3', '7', 'Sta25', '4', 'Sta146', '3', 'Sta130', '3', 'Sta120', '59']
b = ['Dist10', 0,  'Dist10', 0,   'Dist10', 0,   'Dist10', 0,   'Dist10', 0,  'Dist10', 0,   'Dist10', 0,   'Dist5', 0,     'Dist1', 0,   'Dist5', 0,     'Dist5', 0,   'Dist5', 0,   'Dist5', 0,     'Dist5', 0,   'Dist5', 0,   'Dist5', 0,   'Dist5', 0,   'Dist5', 0,   'Dist5', 0,  'Dist5', 0,     'Dist5', 0,    'Dist5', 0,    'Dist8', 0,   'Dist8', 0,   'Dist8', 0,   'Dist1', 0,   'Dist6', 0, 'Dist6', 0,     'Dist6', 0,   'Dist6', 0,    'Dist6', 0]
b = []
for i,val in enumerate(a):
    flag = 0
    with open('./dataFolder/station.csv') as f:
        f = csv.reader(f)
        for row in f:
            if val == row[1]:
                b.append(row[3])
                flag = 1
                break
    if flag == 0:
        b.append(0)
    print('---over---')
print(b)