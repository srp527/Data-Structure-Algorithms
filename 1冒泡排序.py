# -*- coding:utf-8 -*- 
__author__ = 'SRP'

'''冒泡排序（Bubble Sort）

   用时: 14s
   
冒泡排序（Bubble Sort），是一种计算机科学领域的较简单的排序算法。
它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。
这个算法的名字由来是因为越大的元素会经由交换慢慢“浮”到数列的顶端，故名。

# -1 是因为每次比对的都 是i 与i +1,不减1的话,最后一次对比会超出list 获取范围,-j是因为,每一次大loop就代表排序好了一个最大值,放在了列表最后面,下次loop就不用再运算已经排序好了的值 了
        
'''

import random,time,functools
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
def bubble_sort(list):
    '''冒泡排序'''
    n = len(list)
    count = 0
    for j in range(n):
        for i in range(n-j-1):
            if list[i] > list[i+1]:
                tmp = list[i]
                list[i],list[i+1] = list[i+1],tmp
            count += 1
    print('排序后:{0}\n排序次数{1}'.format(list,count))

bubble_sort(list)






# def bubble_sort(list):
#     count = 0
#     for j in range(len(list)):
#         for i in range(len(list) - j -1):
#             if list[i] > list[i+1]:
#                 tmp = list[i]
#                 list[i],list[i+1] = list[i+1],tmp
#                 # print(list)
#             count += 1
#
#     print(list)
#     print(count)
#
# bubble_sort(list)
