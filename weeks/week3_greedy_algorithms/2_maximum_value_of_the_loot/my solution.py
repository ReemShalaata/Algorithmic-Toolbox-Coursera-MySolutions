def max_value_loot(n,W):
    sum1=0
    v=[None]*n
    w=[None]*n
    vw=[None]*n
    for i in range(n):
        v[i],w[i]=input().split()
        vw[i]=float(v[i])/float(w[i])
    
    while(max(vw)!=0):
        maxnum=max(vw)
        for i in range(n):
            if (maxnum==vw[i]):
                index=i
                
        if W>=float(w[index]) and vw[index]!=0:
            sum1=float(v[index])+sum1
            vw[index]=0
            W=W-float(w[index])

        if W<float(w[index])and vw[index]!=0:
            sum1=W*vw[index]+sum1
            vw[index]=0
            W=0
            
        
        

    return sum1

n,W=input().split()
print(max_value_loot(int(n),int(W)))
        
            
