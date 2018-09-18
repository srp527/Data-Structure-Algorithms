# -*- coding:utf-8 -*- 
__author__ = 'SRP'

'''二分查找法'''

# list = [15,2,5,9,8,3,4,52,45,98,67,50,35,14,27,21,5]


# def binary_search(list,find_num):
#     n = len(list)
#     if n > 1:
#         mid = n // 2
#         if list[mid] == find_num:
#             print('找到数字:',list[mid])
#         elif list[mid] > find_num:
#             return binary_search(list[0:mid],find_num)
#         else:
#             return binary_search(list[mid+1:],find_num)
#     else:
#         if list[0] == find_num:
#             print('找到数字了',list[0])
#         else:
#             print('找不到')
#
# list = sorted(list)
# print(list)
# binary_search(list,15)


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


