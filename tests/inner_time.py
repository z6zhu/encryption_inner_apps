import numpy
from numpy import *
#import matplotlib
#import matplotlib.pyplot as plt
# Path hack
import sys, os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(1, os.path.abspath('..'))
import random
import datetime
from fhipe import ipe


fi=open("inner_time","a")
n=int(input("input the row number:"))

lownum=int(input("input the lenght of every low:"))
fi.write(str(n)+"--"+str(lownum)+"---")                                # time
M=20

def load(num):
    if num==1:
        data=[]
        for i in range(n):
            arr=[]
            for j in range(lownum):
                d=random.randint(0,M)
                arr.append(d)
            data.append(arr)
    if num ==2:
        data=[]
        for i in range(n):
            arr=[]
            for j in range(lownum):
                d=random.randint(0,M)
                arr.append(d)
            data.append(arr)
    for line in data:
        for i in line:
            float(i)
    return mat(data)

def pca(dataMat,topNfeat=9999999):
    meanVals=mean(dataMat,axis=0)
    meanRemoved=dataMat-meanVals
    covMat=cov(meanRemoved,rowvar=0)
    eigvals,eigVects=linalg.eig(mat(covMat))
    eigValInd=argsort(eigvals)
    eigValInd=eigValInd[:-(topNfeat+1):-1]
    redEigVects=eigVects[:,eigValInd]
    lowDDataMat=meanRemoved*redEigVects
    reconMat=(lowDDataMat*redEigVects.T)+meanVals
    return lowDDataMat,reconMat

def display(num):
    dataMat=load(num)
    lowDmat,reconMat=pca(dataMat,1)
    #print( ',,,,,,,,,,,,,,,,,,,,,,,,')
   # print( shape(lowDmat))
   # print( "lowDmat:",lowDmat)
    print( "dataMat:")
    print(dataMat)
    return lowDmat
    
def xvectory(a):
    a0=0
    at=[]
    for i in a:
        a0 +=i**2
    a0=numpy.sqrt(a0)
    at.append(a0)
    for i in a:
        at.append(-2*i)
    at.append(1)
    return at

def yvectory(b):
    bn=0
    for i in b:
        bn +=i**2
    bn=numpy.sqrt(bn)
    b.append(bn)
    b.insert(0,1)
    return b
    
if __name__=='__main__':
    
    start=datetime.datetime.now()

    (pp, sk)=ipe.setup(n+2)
    inorout=2 #int(input("please input the number of vertor:"))i
    for i in range(inorout):
        des=[]
        select=int(input("please input the data your want 1 or 2 :"))
        d=load(select) 
        pa=datetime.datetime.now()
        f=pca(d)
        pb=datetime.datetime.now()
        fi.write(str(pb-pa)+"---")                                       # time
        lowdata=display(select)

        for i in lowdata.tolist():
            for j in i:
                des.append(j)
        if select==1:
            xarr=[]

            xa=datetime.datetime.now()
            x=xvectory(des)
            xb=datetime.datetime.now()
            fi.write(str(xb-xa)+"---")                                          # time x 
         
            for i in x:
                xarr.append(int(i))

            keya=datetime.datetime.now()
            skx=ipe.keygen(sk,xarr)
            keyb=datetime.datetime.now()
            fi.write(str(keyb-keya)+"---")                               # time

            ll=0
            tt=[]
            for i in xarr:
                ll+=1
                tt.append(i)
                if ll/10==0:
                    print(tt)
                    tt=[]
                    
            print("x' vectory is ",xarr)
        if select==2:
            yarr=[]
            
            ya=datetime.datetime.now()
            y=yvectory(des)
            yb=datetime.datetime.now()
            fi.write(str(yb-ya)+"---")                                 #time y

            for i in y:
                yarr.append(int(i))

            ena=datetime.datetime.now()
            cty=ipe.encrypt(sk,yarr)
            enb=datetime.datetime.now()
            fi.write(str(enb-ena)+"---")                                        # time   

            print("y' vectory is ",yarr)

    dea=datetime.datetime.now()
    prod=ipe.decrypt(pp,skx,cty,M*M*n)
    deb=datetime.datetime.now()
    fi.write(str(deb-dea)+"---")                                                  # time
    
    end=datetime.datetime.now()                                # all time
    fi.write(str(end-start)+"---")
    fi.write("\n")
    
    print("--------------")
    print("the distance is :",prod) 
    
    
       
    

    


    





