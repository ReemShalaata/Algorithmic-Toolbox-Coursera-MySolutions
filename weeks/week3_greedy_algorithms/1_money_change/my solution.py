def money_change(m):
    num=0
    if int(m//10)!=0:
        num=m//10+num
        m=m%10

    if int(m//5)!=0:
        num=m//5+num
        m=m%5

    return m+num

m=input()
print(money_change(int(m)))
