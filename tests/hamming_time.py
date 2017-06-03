# Path hack
import sys, os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(1, os.path.abspath('..'))

import random
from fhipe import ipe
import datetime
def ipe_hamming(x,y):

  (pp, sk) = ipe.setup(n)

  keya=datetime.datetime.now()
  skx = ipe.keygen(sk, x)
  keyb=datetime.datetime.now()
  f.write(str(keyb-keya)+"---")                            #time 3         

  ena=datetime.datetime.now()
  cty = ipe.encrypt(sk, y)
  enb=datetime.datetime.now()
  f.write(str(enb-ena)+"---")
  
  dea=datetime.datetime.now()
  prod = ipe.decrypt(pp, skx, cty, M*M*n)
  deb=datetime.datetime.now()
  f.write(str(deb-dea)+"---")

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
  
  start=datetime.datetime.now()
  n=int(input("input the  length of vector about hamming:"))
  M = 1
  x=[]
  y=[]
  for i in range(n):
      x=[random.randint(0,M) for i in range(n)]
  for i in range(n):
      y=[random.randint(0,M) for i in range(n)]
  print("the first hamming vector is :",x)
  print("the second hamming vector is :",y)
  
  
   
  cova=datetime.datetime.now()                                         #  time    1
  (x,y)= convert(x,y)
  covb=datetime.datetime.now()

  f=open("hamming_time","a")
  f.write(str(n))
  f.write("---")
  f.write(str(covb-cova)+"---")

  num=ipe_hamming(x,y)
  result=compulate(num,n)
  print("d(x,y):",result)
   
  end=datetime.datetime.now()
  mid=end-start                                                       # time 5
  strmid=str(mid)
  f.write(strmid)
  f.write("\n")

  print(mid)

