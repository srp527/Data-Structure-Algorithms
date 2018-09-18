# -*- coding:utf-8 -*- 
__author__ = 'SRP'

'''快速排序（quick sort）   
   用时: 0s  最快!

设要排序的数组是A[0]……A[N-1]，首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，
然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，这个过程称为一趟快速排序。
值得注意的是，
快速排序不是一种稳定的排序算法，也就是说，多个相同的值的相对位置也许会在算法结束时产生变动　　

注：在待排序的文件中，若存在多个关键字相同的记录，经过排序后这些具有相同关键字的记录之间的相对次序保持不变，
该排序方法是稳定的；若具有相同关键字的记录之间的相对次序发生改变，则称这种排序方法是不稳定的。
要注意的是，
排序算法的稳定性是针对所有输入实例而言的。
即在所有可能的输入实例中，只要有一个实例使得算法不满足稳定性要求，则该排序算法就是不稳定的。
ajax'''

import random,time,functools

list = [15,2,5,9,8,3,4,52,45,98,67,50,35,14,27,21,5]
list2 = [random.randrange(10000) for i in range(10000)]


count = 0
def quick_sort(list):
    '''快排'''
    if list==[]:
        return []
    else:
        pivot = list[0]
        low = quick_sort([x for x in list[1:] if x<pivot])
        high = quick_sort([x for x in list[1:] if x>=pivot])
        global count
        count += 1
        return low + [pivot] + high

print(quick_sort(list2),count)


# n = len(list)
# left = 0
# right = n - 1
# def quick(list,left0,right0):
#     if left0 >= right0:
#         return
#     left = left0
#     right = right0
#
#     tmp = list[left]
#     while left < right:
#         while left < right and list[right] > tmp:
#             right -= 1
#         list[left],list[right] = list[right],tmp
#
#         while left < right and list[left] <= tmp:
#             left += 1
#         list[right],list[left] = list[left],tmp
#     # print(left0,right0)
#     quick(list,left0,left-1)
#     quick(list,left+1,right0)
#
# quick(list,left,right)
#
# print(list)





# def quick(list,left,right):
#     if left >= right:
#         return
#     low,high = left,right
#     key = list[low]
#
#     while low < high:
#         while low < high and list[high] > key:
#             high -= 1
#         list[low] = list[high]
#         list[high] = key
#
#         while low < high and list[low] <= key:
#             low += 1
#         list[high] = list[low]
#         list[low] = key
#
#     quick(list,left,low-1)
#     quick(list,low+1,right)
#
# def quick_sort(list):
#     n = len(list)
#     quick(list,0,n-1)
#     return list
#
# t1 = time.time()
# newlist = quick_sort(list2)
# t2 = time.time()
# print(newlist,t2-t2)




# def quick_sort(list,left,right):
#     '''
#     :param left: 列表的第一个索引
#     :param right: 列表最后一个元素的索引
#     :return:
#     '''
#     if left >= right:
#         return
#     low = left
#     high = right
#     key = list[low]  #第一个值
#
#     while low < high:
#
#         while low < high and list[high] > key: #筛选出右边比key小的数 向下进行 ,只要比key大就一直循环
#             high -= 1
#         #此时直接 把key(array[low]) 跟 比它大的array[high]进行交换
#         list[low] = list[high]
#         list[high] = key
#
#         while low < high and list[low] <= key: #筛选出左边比key大的数 向下进行,只要比key小就一直循环
#             low += 1
#         list[high] = list[low]
#         list[low] = key
#
#     quick_sort(list,left,low-1) #最后用同样的方式对分出来的左边的小组进行同上的做法
#     quick_sort(list,low+1,right) #用同样的方式对分出来的右边的小组进行同上的做法
#
# quick_sort(list,0,len(list)-1)
# print(list)


