# -*- coding:utf-8 -*- 
__author__ = 'SRP'

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
print(a)
print(type(a)) #{"ddf": "你好"}



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