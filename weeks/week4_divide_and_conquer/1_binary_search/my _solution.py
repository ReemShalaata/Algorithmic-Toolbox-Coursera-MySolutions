def binary_search(A,low,high,key):
    if high<low:
        return -1
    mid=int(low +(high-low)/2)
    if key==A[mid]:
        return mid
    if key<A[mid]:
        return binary_search(A,low,mid-1,key)
    if key>=A[mid]:
        return binary_search(A,mid+1,high,key)


A = [int(x) for x in input().split()]
B= [int(x) for x in input().split()]

A=A[1:]
B=B[1:]
low=0
high=len(A)-1

for i in B:
    print(binary_search(A,low,high,i),end =" ")
        
