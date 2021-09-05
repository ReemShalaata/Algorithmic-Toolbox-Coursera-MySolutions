def MaxPairwiseProductNaive1(a,n):
    product=0
    for i in range(n):
        for j in range(n):
            if i!=j and a[i]*a[j]>product:
                product=a[i]*a[j]

    return product

def MaxPairwiseProductNaive(a,n):
    product=0
    for i in range(n):
        for j in range(i+1,n):
            if i!=j and a[i]*a[j]>product:
                product=a[i]*a[j]

    return product


def MaxPairwiseProductFast(a,n):
    index1=0
    for i in range(1,n):
        if a[i]>a[index1]:
            index1=i
            
    if index1==0:
        index2=1
    else: 
        index2=0
        
    for i in  range(1,n):
        if a[i]>a[index2] and i!=index1:
            index2=i
   # print(index1, index2)
    return a[index1]*a[index2]

import random
def StressTest(N,M):
    while True: 
        n=random.randint(2,N)
        a=n*[None]
        for i in range(n):
            a[i]=random.randint(0,M)
        print(a)
        result1=MaxPairwiseProductNaive(a,n)
        result2=MaxPairwiseProductFast(a,n)
        if result1==result2:
            print('OK')
        else:
            print('Wrong answer:',result1,result2)
            break
    return

        
        
if __name__ == '__main__':
    n = int(input())
    a= [int(x) for x in input().split()]
    print(MaxPairwiseProductFast(a,n))




        
