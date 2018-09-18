# -*- coding:utf-8 -*- 
__author__ = 'SRP'

'''堆排序

   用时: 0.06s

堆排序，顾名思义，就是基于堆。因此先来介绍一下堆的概念。
堆分为最大堆和最小堆，其实就是完全二叉树。
最大堆要求节点的元素都要大于其孩子，
最小堆要求节点元素都小于其左右孩子，
两者对左右孩子的大小关系不做任何要求，其实很好理解。
有了上面的定义，我们可以得知，处于最大堆的根节点的元素一定是这个堆中的最大值。
其实我们的堆排序算法就是抓住了堆的这一特点，每次都取堆顶的元素，将其放在序列最后面，
然后将剩余的元素重新调整为最大堆，依次类推，最终得到排序的序列。'''

import random,time,math

list2 = [random.randrange(10000) for i in range(10000)]
list = [15,2,5,9,8,3,4,52,45,98,67,50,35,14,27,21,5]

count = 0
def heap_sort(list):
    n = len(list)
    root = n // 2 - 1
    for i in range(root,-1,-1):
        # print(list)
        sort(list,i,n-1)

    for end in range(n-1,0,-1):
        list[end],list[0] = list[0],list[end]
        # print(list)
        sort(list,0,end-1)

def sort(list,root,end):
    root = root
    while True:
        left = root * 2 + 1
        right = left + 1
        if left > end:
            break
        if right <= end and list[left] < list[right]:
            left += 1
        if list[left] > list[root]:
            list[root],list[left] = list[left],list[root]
            root = left
        else:
            break
        global count
        count += 1

#打印树的一个函数，很好用，谁用谁知道
def print_tree(array): #打印堆排序使用
     '''
     深度 前空格 元素间空格
     1     7       0
     2     3       7
     3     1       3
     4     0       1
     '''
     index = 1
     depth = math.ceil(math.log2(len(array))) # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
     sep = '  '
     for i in range(depth):
         offset = 2 ** i
         print(sep * (2 ** (depth - i - 1) - 1), end='')
         line = array[index:index + offset]
         for j, x in enumerate(line):
             print("{:>{}}".format(x, len(sep)), end='')
             interval = 0 if i == 0 else 2 ** (depth - i) - 1
             if j < len(line) - 1:
                 print(sep * interval, end='')
         index += offset
         print()

print_tree(list)
print('-'*60)
t1 = time.time()
heap_sort(list)
t2 = time.time()
print_tree(list)
print(list,t2-t1,count)


# count = 0
# def heap_sort(list):
#     n = len(list)
#     root = n//2 - 1
#     for i in range(root,-1,-1):
#         sift_down(list,i,n-1)
#
#     for end in range(n-1,0,-1):
#         list[0],list[end] = list[end],list[0]
#         sift_down(list,0,end-1)
#
# def sift_down(list,root,end):
#     root = root
#     while True:
#         child = root * 2 + 1
#         if child > end:
#             break
#
#         if child +1 <= end and list[child] < list[child+1]:
#             child += 1
#
#         if list[child] > list[root]:
#             tmp = list[root]
#             list[root],list[child] = list[child],tmp
#             root = child
#         else:
#             break
#         global count
#         count += 1
#
# t1 = time.time()
# heap_sort(list2)
# t2 = time.time()
# print(list2,t2-t1,count)



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


