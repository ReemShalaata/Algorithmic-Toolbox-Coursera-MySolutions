
# python3
import sys

def compute_min_refills(distance, tank, stops):
    n=len(stops)
    stp=[None]*(n+2)
    stp[0]=0
    stp[n+1]=distance
    for i in range(1,n+1):
        stp[i]=stops[i-1]
    numRefills=0
    currentRefill=0
    while currentRefill<=n:
        lastRefill=currentRefill
        while currentRefill<=n and stp[currentRefill+1]-stp[lastRefill]<=tank:
            currentRefill=currentRefill+1
        
        if currentRefill==lastRefill:
            return -1
        if currentRefill<=n:
            numRefills=numRefills+1
    return numRefills


if __name__ == '__main__':


    distance=input()
    tank=input()
    n=input()
    stops = [int(x) for x in input().split()]
    print(compute_min_refills(int(distance),int( tank), stops))
