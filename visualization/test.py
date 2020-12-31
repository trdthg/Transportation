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
sss(sdict)
