def get_fibonacci_last_digit_naive(n):
    array=[None]*(n+1)
    array[0]=0
    array[1]=1
    for i in range(2,n+1):
        array[i]=(int(array[i-1])+int(array[i-2])%10)
    return array[n]%10

n = int(input())
print(get_fibonacci_last_digit_naive(n))

