# -*- coding:utf-8 -*- 
__author__ = 'SRP'

'''-----------1-----------'''
#定义树结构
class TreeNode(object):
    def __init__(self, val=0, left=0, right=0):
        self.val = val
        self.left = left
        self.right = right


class BTree(object):
    def __init__(self, root=0):
        self.root = root

    #前序遍历
    def preOrder(self, treenode):
        if treenode is 0:
            return
        print(treenode.val)
        self.preOrder(treenode.left)
        self.preOrder(treenode.right)

    #中序遍历
    def inOrder(self, treenode):
        if treenode is 0:
            return
        self.inOrder(treenode.left)
        print(treenode.val)
        self.inOrder(treenode.right)

    #后序遍历
    def postOrder(self, treenode):
        if treenode is 0:
            return
        self.postOrder(treenode.left)
        self.postOrder(treenode.right)
        print(treenode.val)


if __name__ == '__main__':
    n1 = TreeNode(val=1)
    n2 = TreeNode(2, n1, 0)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5, n3, n4)
    n6 = TreeNode(6, n2, n5)
    n7 = TreeNode(7, n6, 0)
    n8 = TreeNode(8)
    root = TreeNode('root', n7, n8)

    bt = BTree(root)
    print("preOrder".center(50, '-'))
    print(bt.preOrder(bt.root))

    print("inOrder".center(50, '-'))
    print(bt.inOrder(bt.root))

    print("postOrder".center(50, '-'))
    print(bt.postOrder(bt.root))


'''---------2---------'''

#定义二叉树结构
class TreeNode(object):

    def __init__(self, root=None,left=None,right=None):
        self.root = root
        self.left = left
        self.right = right


#创建二叉树
class Tree(object):

    def __init__(self,data_list):
        self.it = iter(data_list)

    def createTree(self,bt=None):
        try:
            next_num = next(self.it)
            if next_num is '#':
                bt = None
            else:
                bt = TreeNode(next_num)
                bt.left = self.createTree(bt.left)
                bt.right = self.createTree(bt.right)
        except Exception as e:
            print(e)
        return bt

    #前序遍历
    def preOrderTrave(self,bt):
        if bt is not None:
            print(bt.root,end=' ')
            self.preOrderTrave(bt.left)
            self.preOrderTrave(bt.right)

    #中序遍历
    def inOrderTrave(self,bt):
        if bt is not None:
            self.inOrderTrave(bt.left)
            print(bt.root,end=' ')
            self.inOrderTrave(bt.right)

    #后序遍历
    def postOrderTrave(self,bt):
        if bt is not  None:
            self.postOrderTrave(bt.left)
            self.postOrderTrave(bt.right)
            print(bt.root,end=' ')

    #test
    def printTrave(self,bt):
        print('先序遍历:',end='')
        self.preOrderTrave(bt)
        print('\n中序遍历:',end='')
        self.inOrderTrave(bt)
        print('\n后序遍历:',end='')
        self.postOrderTrave(bt)

    # 最大深度
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count = 0
        if root == None:
            return 0
        if root:
            ldepth = self.maxDepth(root.left)
            rdepth = self.maxDepth(root.right)
            count = ldepth + 1 if ldepth > rdepth else rdepth + 1
        return count

# data = input('请输入value:')
data_list = [5,4,6,'#','#','#',2,3,'#','#',1,'#']
# data_list = list(data)
tree = Tree(data_list)

root = tree.createTree()
tree.printTrave(root)
print('\n最大深度:',tree.maxDepth(root))

'''
请输入value:abd#g###ce##fh###
先序遍历:a b d g c e f h 
中序遍历:d g b a e c h f 
后序遍历:g d b e h f c a 
'''