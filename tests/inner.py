import numpy,math
from numpy import *
#import matplotlib
#import matplotlib.pyplot as plt
# Path hack
import sys, os
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(1, os.path.abspath('..'))
import random
from fhipe import ipe
n=int(input("the number of  lows:"))
lownum=int(input("the lenght of every low:"))
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
        a0 +=i*i
    at.append(a0)
    for i in a:
        at.append(-2*i)
    at.append(1)
    return at

def yvectory(b):
    bn=0
    for i in b:
        bn +=i*i
    b.append(bn)
    b.insert(0,1)
    return b
    
if __name__=='__main__': 
    (pp, sk)=ipe.setup(n+2)
    inorout=2 #int(input("please input the number of vertor:"))
    for i in range(inorout):
        des=[]
        select=int(input("please input the data your want 1 or 2 :"))
        d=load(select)
        f=pca(d)
        lowdata=display(select)
        for i in lowdata.tolist():
            for j in i:
                des.append(j)
        print("x vectory is ",des)
        if select==1:
            xarr=[]
            x=xvectory(des)
            for i in x:
                xarr.append(int(i))
            skx=ipe.keygen(sk,xarr)
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
            y=yvectory(des)
            for i in y:
                yarr.append(int(i))
            cty=ipe.encrypt(sk,yarr)
            print("y' vectory is ",yarr)

    prod=ipe.decrypt(pp,skx,cty,10*M*M*n)
    print(prod)
    print("--------------")
    print("the distance is :",math.sqrt(prod)) 
    
    
        
    

    


    





