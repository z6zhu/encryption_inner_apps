# Path hack
import sys, os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(1, os.path.abspath('..'))

import random
import math
from fhipe import ipe
import datetime
def ipe_decry_m(xvec,yvec,dev):

  (pp, sk) = ipe.setup(len(xvec))

  kea=datetime.datetime.now()
  skx = ipe.keygen(sk, xvec)
  keb=datetime.datetime.now()
  f.write(str(keb-kea)+"---")                        # time
  
  ena=datetime.datetime.now()
  cty = ipe.encrypt(sk, yvec)
  enb=datetime.datetime.now()
  f.write(str(enb-ena)+"---")                              # time

  dea=datetime.datetime.now()
  prod = ipe.decrypt(pp, skx, cty, M*M*n)
  deb=datetime.datetime.now()
  f.write(str(deb-dea)+"---")                             # time

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
  sumx=0
  sumy=0
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
  return x,y,meanx,meany

def convertfloat(xvec,yvec):
  x=[]
  y=[]
  sumx=0
  sumy=0
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

  start=datetime.datetime.now()
  n=int(input("input the  number of every vector line about regression:"))
  M = 20
  t=[]
  k=[]
  for i in range(n):
      x=random.randint(0,M) 
      t.append(float(x))
  for i in range(n):
      x=random.randint(0,M)
      k.append(float(x))
  f=open("regression_time","a")
  f.write(str(n)+"---")
  
  deva=datetime.datetime.now()
  dev=deviation(t)
  devb=datetime.datetime.now()
  f.write(str(devb-deva)+"---")                                    # time  1
  
  cova=datetime.datetime.now()
  (x1,y1,meanx,meany)=convert(t,k) # is used                              #time  2
  covb=datetime.datetime.now()
  f.write(str(covb-cova)+"---")
  
  ma=datetime.datetime.now()
  m=int(ipe_decry_m(x1,y1,dev))
  mb=datetime.datetime.now()
  f.write(str(mb-ma)+"--------")                                 # time
  
  getca=datetime.datetime.now()
  c=int(ipe_to_c(m,meanx,meany))
  getcb=datetime.datetime.now()
  f.write(str(getcb-getca))                                               #time  6

  print("the value of b is :",c)
  if int(c)==0:
      print("y=",m,"x")
  else: 
      print("y=",m,"x+(",c,")")
  

  end=datetime.datetime.now()
  f.write(str(end-start))                                         # time 7 
  f.write("\n")

