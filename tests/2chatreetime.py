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
import time

time_list=[]


time_start=time.time()         #start -----------------------------------------
all_time=[]

N=30
f=lambda x,y: 1 if x<y else 0



set=[]
set_time=time.time()
(pp,sk)=tife.setup(N,f)
set_over=time.time()
set_diff=set_over-set_time
set.append(set_time)
set.append(set_over)
set.append(set_diff)
time_list.append(set)

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
            if tife.decrypt(pp,node.value[0],n.value)==1: # this  is  compare

                if n.left == None:
                    node.parent = n
                    n.left = node
                    node.value=node.value[1]  # right cipher 
                    break
                else:
                    n = n.left
            if tife.decrypt(pp,node.value[0],n.value)==0:  # compare+
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
    for i in range(1):
        en=[]  
        en_time=time.time()
        x=random.randint(0,N-1)
        ctx=tife.encryptL(sk,x)
        cty=tife.encryptR(sk,x)
        en_over=time.time()
        en_diff=en_over-en_time
        en.append(en_time)
        en.append(en_over)
        en.append(en_diff)
        time_list.append(en)

        cipher=[ctx,cty]
        array.append(cipher)
    bt = BTree()
    for ctxt in array :
        de_insert=[]
        de_insert_time=time.time()
        bt.insert(Node(ctxt))  # as client
        de_insert_over=time.time()
        de_insert_diff=de_insert_over-de_insert_time
        de_insert.append(de_insert_time)
        de_insert.append(de_insert_over)
        de_insert.append(de_insert_diff)
        time_list.append(de_insert)
    time_over=time.time()
    time_diff=time_over-time_start
    all_time.append(time_start)
    all_time.append(time_over)
    all_time.append(time_diff)
    time_list.append(all_time)
    print("setup                 time",time_list[0])
    print("encryption            time",time_list[1])
    print("decryption and insert time",time_list[2])
    print("all                   time",time_list[3])
