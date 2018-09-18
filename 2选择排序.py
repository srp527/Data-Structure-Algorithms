# -*- coding:utf-8 -*- 
__author__ = 'SRP'

'''   选择排序    

      用时: 10.6s
      
  算法的工作方式是选择最小的未排序项，然后将其与下一个要填充的项进行交换。
  选择排序的工作方式如下:查找整个数组中最小的元素，一旦找到，就将它(最小的元素)
  与数组的第一个元素交换。然后在剩余的数组中查找最小的元素(没有第一个元素的数组)，
  并将其与第二个元素交换。然后在剩余的数组中查找最小的元素(没有第一个和第二个元素的数组)，
  并与第三个元素交换，以此类推。
  这是一个例子,
  '''

import random,time
list2 = [random.randrange(10000) for i in range(10000)]
list = [15,2,5,9,8,3,4,52,45,98,67,50,35,14,27,21,5]


# count = 0
# min_num_index = 0 #初始列表最小值,默认为第一个
# for j in range(len(list)):
#     for i in range(j,len(list)):
#         if min_num_index < j:
#             min_num_index = j
#         if list[i] < list[min_num_index]:
#             print('-------------------------------------')
#             print('min_num_index:%s'%min_num_index)
#             min_num_index = i
#             print('j-i :%s-%s'%(j,i))
#             print('--->',list[i],list[min_num_index])
#             print('-------------------------------------')
#         count += 1
#     else:
#         print('======================================')
#         print('最小值为: %s; j-min_num_index:%s-%s' %(list[min_num_index],j,min_num_index))
#         tmp = list[min_num_index]
#         list[min_num_index] = list[j]
#         list[j] = tmp
#         print(list)
#         print('======================================')
#
# print(list)
# print(count)

