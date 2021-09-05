### Uses python3
import sys
import numpy as np
def optimal_weight(W, w,n):

    value=np.zeros((len(w)+1,W+1))
    for i in range(1,n+1):

        for ww in range(1,W+1):
        
            value[i,ww]=value[i-1,ww]
            if w[i-1]<=ww:
                val=value[i-1,ww-w[i-1]]+w[i-1]
                if value[i,ww]<val:
                   value[i,ww]=val
    return value[n,W]



if __name__ == '__main__':
    input = sys.stdin.read()
    W,n,*w=list(map(int, input.split()))

    print(int(optimal_weight(W, w,n)))
