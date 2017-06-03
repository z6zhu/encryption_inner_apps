# Path hack
import sys, os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(1, os.path.abspath('..'))

import random
from fhipe import ipe

def ipe_hamming(x,y):

  (pp, sk) = ipe.setup(n)
  skx = ipe.keygen(sk, x)
  print("the skx is:",skx)
  cty = ipe.encrypt(sk, y)
  print("the cty is:",cty)
  prod = ipe.decrypt(pp, skx, cty, M*M*n)
  print("<X',Y'> :",prod)
  return prod
def convert(xvec,yvec):
  x=[]
  y=[]
  for i in xvec:
      if i ==0:
          i=-1
      x.append(i)
  for i in yvec:
      if i==0:
          i=-1
      y.append(i)
  return x,y
          
def compulate(num,n):
  return float(n-num)/2

  
if __name__=='__main__':
  n=int(input("input the  length of vector about hamming:"))
  M = 1
  x=[]
  y=[]
  for i in range(n):
      data=int(input("input the first vector :"))
      x.append(data)
  for i in range(n):
      data=int(input("input the second vector:"))
      y.append(data)
  print("the first hamming vector is :",x)
  print("the second hamming vector is :",y)
  (x,y)= convert(x,y)
  num=ipe_hamming(x,y)
  result=compulate(num,n)
  print("d(x,y):",result)
   


