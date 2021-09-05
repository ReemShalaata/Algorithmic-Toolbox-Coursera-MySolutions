
import sys
import numpy as np
from numpy import random
import itertools

def optimal_weight(W, w,n):

    value=np.zeros((len(w)+1,W+1))
    for i in range(1,n+1):

        for ww in range(1,W+1):
        
            value[i,ww]=value[i-1,ww]
            if w[i-1]<=ww:
                val=value[i-1,ww-w[i-1]]+w[i-1]
                if value[i,ww]<val:
                   value[i,ww]=val
    return value

def new_w(value,w,num):
    row=len(w)
    col=num
    indexes=[]
   
    while(row>0 and col>0):
        
        if(value[row,col]==value[row-1,col]):
            row=row-1
        
        elif value[row-1,col-w[row-1]]+w[row-1]>=value[row-1,col] or(row==1 and col==w[0]):#we 
            indexes.append(row-1)
            col=col-w[row-1]
            row =row-1

          
        elif value[row-1,col-w[row-1]]+w[row-1]<value[row-1,col]:#dont use row item
            row=row-1
            
    for index in indexes:
        del w[index]         
   
    return w

def partition3(A):
    sum1=sum(A)            
    if (len(A)<3) or ((sum1%3)!=0) :
        return 0
        
    elif (sum1%3==0 and A==[A[0]]*len(A) and (len(A)%3)!=0):
        return 0
    
    elif (sum1%3==0 and A==[A[0]]*len(A) and (len(A)%3)==0):
        return 1
                
    

    elif (sum1%3==0 and (len(A)!=0)):
        count=0
        ValueMatrix=optimal_weight(sum1//3, A,len(A))

        for i in range(1,len(A)+1):
            if ValueMatrix[i,sum1//3]:
                count+=1
        if count>=3:
             return 1 
        else:
            return 0

 


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

