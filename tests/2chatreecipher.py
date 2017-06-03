"""
Copyright (c) 2016, zhuzhu
 

Two-input functional encryption,and use it to  query and sort
"""

# Path hack
import sys, os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(1, os.path.abspath('..'))

import random
from fhipe import  tife

N=30
def f(x,y):
    if x<y:
        return -1
    elif x>y:
        return 1
    else:
        return 0
(pp,sk)=tife.setup(N,f)
class Node(object):
    def __init__(self, v = None, left = None, right=None, parent=None):
        self.value = v
        self.left = left
        self.right = right
        self.parent = parent
class BTree(object):
    def __init__(self):
        self.root = None
        self.size = 0
    def insert(self, node):  #  as  server 
        n = self.root
        if n == None:
            node.value=node.value[1]    # input right cihper
            self.root = node # first time  inset cipher
            return  
        while True:
            if tife.decrypt(pp,node.value[0],n.value)==-1: # this  is  compare
                if n.left == None:
                    node.parent = n
                    n.left = node
                    node.value=node.value[1]  # right cipher 
                    break
                else:
                    n = n.left
            if tife.decrypt(pp,node.value[0],n.value)==1:  # compare+
                if n.right == None:
                    n.parent = n
                    n.right = node
                    node.value=node.value[1]   # right cipher
                    break
                else:
                    n = n.right
    def find(self, v):
        n = self.root # http://yige.org
        while True:
            if n == None:
                return None
            if v == n.value:   
                return n
            if v < n.value:
                n = n.left
                continue
            if v > n.value:
                n = n.right
    def find_successor(node):
        assert node != None and node.right != None
        n = node.right
        while n.left != None:
            n = n.left
        return n
    def findroot(self):
        return self.root
    def Order(self,treenode):
        if treenode is None:
            return
        self.Order(treenode.left)
        print(treenode.value)
        self.Order(treenode.right)
if __name__ == '__main__':
    array=[]
    for i in range(5):
        x=random.randint(0,N-1)
        ctx=tife.encryptL(sk,x)
        cty=tife.encryptR(sk,x)
        cipher=[ctx,cty]
        array.append(cipher)
    bt = BTree()
    for ctxt in array :
        bt.insert(Node(ctxt))  # as client
    bt.Order(bt.findroot())
