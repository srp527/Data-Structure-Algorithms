# -*- coding:utf-8 -*- 
__author__ = 'SRP'


'''插入排序(Insertion Sort)

插入排序(Insertion Sort)的基本思想是：将列表分为2部分，左边为排序好的部分，
右边为未排序的部分，循环整个列表，每次将一个待排序的记录，
按其关键字大小插入到前面已经排好序的子序列中的适当位置，直到全部记录插入完成为止。'''

import random
import time
import functools

list2 = [random.randrange(10000) for i in range(10000)]
list = [15,2,5,9,8,3,4,52,45,98,67,50,35,14,27,21,5]

def run_time():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            t1 = time.time()
            func(*args,**kwargs)
            t2 = time.time()
            print('<%s>用时:%s' %(func.__doc__,t2-t1))
        return wrapper
    return decorator

@run_time()
def insert_sort(list):
    '''插入排序'''
    count = 0
    n = len(list)
    for i in range(1,n):
        tmp = list[i]
        position = i
        while position > 0 and list[position-1] > tmp:
            list[position],list[position-1] = list[position-1],tmp
            position -= 1
            count += 1
    print('排序后:{0} \n排序次数:{1}'.format(list,count))

insert_sort(list)




# count = 0
# for i in range(1,len(list)):
#     num = list[i]  #先记下来每次大循环走到的第几个元素的值
#     position = i
#     # print('num:%s,position:%s'%(num,position))
#
#     while position > 0 and list[position-1] > num: #当前元素的左边的紧靠的元素比它大,要把左边的元素一个一个的往右移一位,给当前这个值插入到左边挪一个位置出来
#         list[position] = list[position-1]
#         position -= 1
#         count += 1
#         # print('--->',list)
#
#     # print('num:%s,position:%s' % (num, position))
#     list[position] = num
# print(list)
# print(count)
