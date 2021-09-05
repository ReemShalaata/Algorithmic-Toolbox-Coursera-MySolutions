def Primitive_calculater(n):
    min_steps=[0]*(n+1)
    min_steps[0]=0
    min_steps[1]=0
    for i in range(2,n+1):
        min_steps[i]=1000000*n
        x=i
        
        if x%3==0:
            count=min_steps[x//3]+1
            if count< min_steps[i]:
                min_steps[i]=count
               
        if x%2==0:
            count=min_steps[x//2]+1
            if count< min_steps[i]:
                 min_steps[i]=count
             
        if (x%3!=0):
            count=min_steps[x-1]+1
            if count< min_steps[i]:
                min_steps[i]=count
               
              

    numbers=[None]*(min_steps[n]+1)
    numbers[0]=1
    numbers[min_steps[n]]=n

    for j in range(len(numbers)-2,0,-1):    

            if(numbers[j+1]%3==0 ):
                numbers[j]=numbers[j+1]//3
            elif (numbers[j+1]%2==0 and min_steps[numbers[j+1]//2]<min_steps[numbers[j+1]-1]):
                numbers[j]=numbers[j+1]//2
            else:
                numbers[j]=numbers[j+1]-1
           
                
    return min_steps[n], numbers        
n=int(input())
minsteps,mat=Primitive_calculater(n)
print(minsteps)
for i in mat:
    print(int(i),end=" " )
           
