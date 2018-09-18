# -*- coding:utf-8 -*- 
__author__ = 'SRP'

'''希尔排序（shell sort）
   插入排序用时  7.1s
   希尔排序用时  1.1s

希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本,
该方法的基本思想是：先将整个待排元素序列分割成若干个子序列（由相隔某个“增量”的元素组成的）
分别进行直接插入排序，然后依次缩减增量再进行排序，待整个序列中的元素基本有序（增量足够小）时，
再对全体元素进行一次直接插入排序。因为直接插入排序在元素基本有序的情况下（接近最好情况），
效率是很高的，因此希尔排序在时间效率比直接插入排序有较大提高


'''

import random,time
list2 = [random.randrange(10000) for i in range(10000)]
list = [15,2,5,9,8,3,4,52,45,98,67,50,35,14,27,21,5]

def shell_sort(list):
    n = len(list)
    step = n // 2
    while step > 0:
        for i in range(n):
            if i+step < n :
                if list[i] > list[i+step]:
                    list[i],list[i+step] = list[i+step],list[i]
        step = step // 2
    #-----------------------------#
    for i in range(n):
        num = list[i]
        postion = i
        while postion > 0 and list[postion-1] > num:
            list[postion],list[postion-1] = list[postion-1],num
            postion -= 1

newlist = shell_sort(list)
print(list)





# def shell_sort(list):
#     n = len(list)
#     step = n//2
#     while step > 0:
#         for i in range(n):
#             if i+step < n:
#                 if list[i] > list[i+step]:
#                     tmp = list[i]
#                     list[i] = list[i+step]
#                     list[i+step] = tmp
#         step = step//2
#     #---------------------------#
#     for i in range(1,n):
#         tmp = list[i]
#         index = i
#         while i > 0 and list[index-1] > tmp:
#             list[i],list[index-1] = list[index-1],tmp
#
#     return list
#
# newlist = shell_sort(list)
# print(newlist)




# def shell_sort(list):
#     step = len(list)//2
#     while step > 0:
#         for i in range(len(list)):
#             if i + step < len(list):
#                 if list[i] > list[i+step]:
#                     tmp = list[i]
#                     list[i],list[i+step] = list[i+step],tmp
#         step = step//2
#
#     # print(list)
#     for i in range(1,len(list)):
#         num = list[i]
#         position = i
#
#         while position > 0 and list[position -1] > num:
#             list[position],list[position-1] = list[position-1],num
#             position -= 1
#
# t1 = time.time()
# shell_sort(list2)
# t2 = time.time()
# print(list2,t2-t1)









