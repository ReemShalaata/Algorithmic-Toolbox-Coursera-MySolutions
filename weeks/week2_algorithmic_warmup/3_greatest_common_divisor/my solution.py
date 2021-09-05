def GCD(a,b):
    if b==0:
        return a
    return GCD(b,a%b)

a,b=input().split()

print(GCD(int(a),int(b)))
