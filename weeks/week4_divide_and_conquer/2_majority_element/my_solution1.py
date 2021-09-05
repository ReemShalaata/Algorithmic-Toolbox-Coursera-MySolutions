
            
def Maj(A):
    m=-1
    a_dict={}
    for i in range(len(A)):
        a_dict[A[i]]=0
    for i in range(len(A)):
        a_dict[A[i]]+=1
    for key, value in a_dict.items():
        if value>m:
            m=value
    if m>len(A)//2:
        return 1
    return 0
        
        
        
        
    
    
n=int(input())
A= [int(x) for x in input().split()]

print(Maj(A))
