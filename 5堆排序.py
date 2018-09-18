# -*- coding:utf-8 -*- 
__author__ = 'SRP'

'''堆排序

   用时: 0.06s

堆排序，顾名思义，就是基于堆。因此先来介绍一下堆的概念。
堆分为最大堆和最小堆，其实就是完全二叉树。最大堆要求节点的元素都要大于其孩子，
最小堆要求节点元素都小于其左右孩子，两者对左右孩子的大小关系不做任何要求，其实很好理解。
有了上面的定义，我们可以得知，处于最大堆的根节点的元素一定是这个堆中的最大值。
其实我们的堆排序算法就是抓住了堆的这一特点，每次都取堆顶的元素，将其放在序列最后面，
然后将剩余的元素重新调整为最大堆，依次类推，最终得到排序的序列。'''

import random,time
list2 = [random.randrange(10000) for i in range(10000)]
list = [15,2,5,9,8,3,4,52,45,98,67,50,35,14,27,21,5]



















def sift_down(list,root,end):
    root = root
    while True:
        child = root * 2 + 1
        if child > end:
            break

        if child +1 <= end and list[child] < list[child+1]:
            child += 1

        if list[child] > list[root]:
            tmp = list[root]
            list[root],list[child] = list[child],tmp
            root = child
        else:
            break

def heap_sort(list):
    n = len(list)
    root = n//2 - 1
    for i in range(root,-1,-1):
        sift_down(list,i,n-1)

    for end in range(n-1,0,-1):
        list[0],list[end] = list[end],list[0]
        sift_down(list,0,end-1)

t1 = time.time()
heap_sort(list2)
t2 = time.time()
print(list2,t2-t1)










# import time,random
# def sift_down(list,node,end):
#     root = node  # index-v :7 - 52
#     while True:
#         child = root*2 + 1  #index-v : 15 - 21
#         if child > end:  # end = 16
#             break
#         print('root-v: %s-%s,chile-v: %s-%s'%(root,list[root],child,list[child]))
#         print(list)
#
#         if child +1 <= end and list[child] < list[child + 1]:
#             child += 1
#
#         if list[root] < list[child]:
#             tmp = list[root]
#             list[root] = list[child]
#             list[child] = tmp
#             root = child
#         else:
#             break
#     print('-----------------------------')
#
# def heap_sort(list):
#     first = len(list)//2 -1   # 7
#     for i in  range(first,-1,-1):
#         print(i)
#         sift_down(list,i,len(list)-1)
#     print('----------end-----------',list)
#
#     for end in range(len(list)-1,0,-1):
#         list[0],list[end] = list[end],list[0]
#         sift_down(list,0,end-1)
#
# heap_sort(list)
# print(list)


