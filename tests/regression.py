# Path hack
import sys, os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(1, os.path.abspath('..'))

import random
import math
from fhipe import ipe

def ipe_decry_m(xvec,yvec,dev):

  (pp, sk) = ipe.setup(len(xvec))
  skx = ipe.keygen(sk, xvec)
  cty = ipe.encrypt(sk, yvec)
  prod = ipe.decrypt(pp, skx, cty, M*M*n)
  m=prod/(len(xvec)*dev*dev)
  return m
def ipe_to_c(value,x,y):
  c=y-value*x
  return c
def deviation(xvec):
  sumn =0
  devsum=0
  for i in xvec:
      sumn +=i
  mean=sumn/len(xvec)
  for i in range(len(xvec)):
      a=(xvec[i]-mean)*(xvec[i]-mean)
      devsum+=a    
  b=devsum/len(xvec)
  dev=math.sqrt(b)
  return dev    
def convert(xvec,yvec):
  x=[]
  y=[]
  x1=[]
  y1=[]
  sumx=0.0
  sumy=0.0
  for i in xvec:
      sumx +=i
  meanx=sumx/len(xvec)
  for i in yvec:
      sumy +=i
  meany=sumy/len(yvec)
  for i in xvec:
      x.append(int(i-meanx))
  for i in yvec:
      y.append(int(i-meany))
  for i in xvec:
      x1.append(i-meanx)
  for i in yvec:
      y1.append(i-meany)
  return x1,y1,x,y,meanx,meany
def convertfloat(xvec,yvec):
  x=[]
  y=[]
  sumx=0.0
  sumy=0.0
  for i in xvec:
      sumx +=i
  meanx=sumx/len(xvec)
  for i in yvec:
      sumy +=i
  meany=sumy/len(yvec)
  for i in xvec:
      x.append(i-meanx)
  for i in yvec:
      y.append(i-meany)
  return x,y,meanx,meany


  
if  __name__=='__main__':
  n=int(input("input the length of vector about regression:"))
  M = 10
  t=[]
  k=[]
  x=[]
  y=[]
  for i in range(n):
      data=float(input("input the first vector:"))
      t.append(data)
  for i in range(n):
      data=float(input("input the second vector:"))
      k.append(data)
  j=0
  q=0
  for i in t:
      j+=1
      if j<4:
          x.append(i)
  for i in k:
      q+=1
      if q<4:
          y.append(i)
  dev=deviation(x)
  (x1,y1,x,y,meanx,meany)=convert(x,y) # is used
  (tx1,ty1,tx,ty,tmeanx,tmeany)=convert(t,k) # is used
  m=ipe_decry_m(x,y,dev)
  print("the x vector is :",t)
  print("the y vector is :",k)
  print("the x' vector is :",tx1)
  print("the y' vector is :",ty1)
  print("the value of a is :",m)
  c=ipe_to_c(m,meanx,meany)
  print("the value of b is :",c)
  if int(c)==0.0:
      print("y=",m,"x")
  else: 
      print("y=",m,"x+(",c,")")
  

   


