

def GCD_Fast(a,b):
    list=None
    while(b!=0):
        x=a
        z=b
        a=z
        b=x%z
    return a

def lcm(a,b):
    return ((a*b)//GCD_Fast(a,b))

if __name__ == '__main__':
    a,b=input().split()
    print(lcm(int(a),int(b)))


