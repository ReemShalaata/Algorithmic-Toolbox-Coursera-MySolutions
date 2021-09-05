
def DP_Money_Change(money):
    MinNumCoins_Matrix=[0]*(money+1)
    coins_matrix=[1,3,4]
    for m in range(1,money+1):
        MinNumCoins_Matrix[m]=money*10
        for coin in coins_matrix:
            if m>=coin:
                NumCoins=MinNumCoins_Matrix[m-coin]+1
                if NumCoins<MinNumCoins_Matrix[m]:
                    MinNumCoins_Matrix[m]=NumCoins
                
    return  MinNumCoins_Matrix[m]

money=int(input())
print(DP_Money_Change(money))

    
