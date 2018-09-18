# -*- coding:utf-8 -*- 
__author__ = 'SRP'

''' 需求得到任意一个月有几个周一

    1.先得到这一个月有多少天 
    2.weekday()可以判断 年月日为周几 ,循环每一天,结果为0 的即为周一 

'''

# import datetime
# import calendar
#
# while True:
#     try:
#         date = input('请输入日期[xxxx(年)-xx(月)]:')
#         y,m = (int(i) for i in date.split('-'))
#         # print('y-m:%s-%s' %(y,m))
#         monthRange = calendar.monthrange(y,m)
#         # print(monthRange)  #(6, 31)
#         m1,d = monthRange  #m1 是该月的第一天是星期几
#         # print('m1-d:%s-%s'%(m1,d)) # 6,31
#         count = 0
#         list =[]
#         for i in range(1,d+1):
#             targetDay = datetime.date(y,m,i) # 将输入的日期格式化成标准的日期
#             week = targetDay.weekday()    #判断这一天为周几
#             if week == 0:
#                 list.append(i)
#                 count += 1
#         print('{0}年{1}月 共有{2}个周一\n分别是{3}'.format(y,m,count,list))
#     except Exception as e:
#         print(e)

'''二分查找法'''

list = [15,2,5,9,8,3,4,52,45,98,67,50,35,14,27,21,5]


def binary_search(list,find_num):
    n = len(list)
    if n > 1:
        mid = n // 2
        if list[mid] == find_num:
            print('找到数字:',list[mid])
        elif list[mid] > find_num:
            return binary_search(list[0:mid],find_num)
        else:
            return binary_search(list[mid+1:],find_num)
    else:
        if list[0] == find_num:
            print('找到数字了',list[0])
        else:
            print('找不到')

list = sorted(list)
print(list)
binary_search(list,15)


# def binary_search(num_list, x):
#     '''
#     二分查找
#     '''
#     num_list=sorted(num_list)
#     left, right = 0, len(num_list)
#     while left < right:
#         mid = (left + right) / 2
#         if num_list[mid] > x:
#             right = mid
#         elif num_list[mid] < x:
#             left = mid + 1
#         else:
#             return '待查元素{0}在列表中下标为：{1}'.format(x, mid)
#     return  '待查找元素%s不存在指定列表中'%x

# import os
# dir_path = os.path.dirname(os.path.abspath(__file__))
# print([i for i in os.walk(top=dir_path)])


import json
from json import JSONEncoder
from datetime import datetime

class ComplexEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return super(ComplexEncoder,self).default(obj)
d = { 'name':'alex','data':datetime.now()}
print(json.dumps(d,cls=ComplexEncoder))


# a=json.dumps({"ddf":"你好"},ensure_ascii=False)
a=json.dumps({"ddf":"你好"})
print(a)
a = json.loads(a)

print(type(a)) #{"ddf": "你好"}