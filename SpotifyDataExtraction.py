import json
import csv
 
with open('0/show_60Co02kHGFyvneYPY4NPZS/76pRE1NO1ATRU2fJqWoxXP.json') as json_file:
    data = json.load(json_file)


# nd = data['results']
# print(type(nd))
# print(nd)
# for t in nd:
#     print(t)
# print(type(t))

# print(t)

# finall = t['alternatives']
# print(finall)

# print(type(finall))
# for g in finall:
#     print(g)
# print(type(g))    

# gg = g['transcript']

# print(gg)
######################################################
# new_data = data['var1']

# for t in new_data:
#     print(t)
# print(type(t))    

# final_data = t['var2']
# print(type(final_data))

# for g in final_data:
#     print(g)
#     print(type(g))

# transcript = g['tran']
# print(type(transcript))
# print(transcript)

def extraction():
    nd = data['results']
    for t in nd:
        finall = t['alternatives']
        for g in finall:
            gg = g['transcript']
            print(gg)

extraction()


