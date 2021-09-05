
#import timeit

#start = timeit.default_timer()

'''def partition3_timeexceed(A,l,r):
    x=A[l]
    j=l
    for i in range(l+1,r):
        if A[i]<=x:
            j=j+1
            A[i],A[j]=A[j],A[i]
    A[l],A[j]=A[j],A[l]
    p_end=p_start=j
    k=1
    i=0
    while(p_end-k-i>1):
        if A[i]==x and i<p_end-k and A[p_end-k]!=x:
            p_start=p_end-k
            A[i],A[p_start]=A[p_start],A[i]
            k=k+1
        if A[i]==x  and A[i+1]!=x and A[p_end-k]!=x:
            A[i],A[i+1]=A[i+1],A[i]
        i=i+1
               
    return p_start8,p_end'''


def partition3(A,l,r):
    s=l
    m=0
    j=1
    for i in range(l+1,r+1):
            if A[i]<=A[l]:
                s=s+1
                A[i],A[s]=A[s],A[i]
    A[l],A[s]=A[s],A[l]

    for j in range(l,s) :
        if A[j]==A[s] and j<s-m:
            m=m+1
            A[j],A[s-m]=A[s-m],A[j]
        j=j+1

    return s-m,s
        
def improved_QuickSort(A,l,r):
    if l>=r :
        return
    p1,p2=partition3(A,l,r)

    improved_QuickSort(A,l,p1-1)
    improved_QuickSort(A,p2+1,r)

n=int(input())
A= [int(x) for x in input().split( )]
improved_QuickSort(A,0,n-1)
for i in A :
    print(i, end=" ")


#stop = timeit.default_timer()

#print('Time: ', stop - start)  

