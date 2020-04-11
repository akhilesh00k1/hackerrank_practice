def func(n):
    prime=[1 for i in range(n+1)]
    prime[0]=0
    prime[1]=0
    
    for i in range(2,n+1):
        if prime[i] ==1:
            for j in range(2,n//2):
                if i*j<=n:
                    prime[i*j]=0
    return prime
n=int(input())        
print(func(n))        

