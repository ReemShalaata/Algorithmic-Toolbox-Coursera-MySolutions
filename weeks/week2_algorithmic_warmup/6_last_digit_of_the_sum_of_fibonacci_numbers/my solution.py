def get_fibonacci_last_digit_naive(n):
    array=[None]*(n+1)
    array[0]=0
    array[1]=1
    for i in range(2,n+1):
        array[i]=(int(array[i-1])+int(array[i-2]))%10
    return array[n]%10


def fibonacci_sum(n):
    sum=0
    for i in range(0,n/2):
        sum= (get_fibonacci_last_digit_naive(n) +sum)%10

    for i in range(n/2+1,n):
        sum= (get_fibonacci_last_digit_naive(n) +sum)%10


    return sum
n=int(input())
print(fibonacci_sum(n))

