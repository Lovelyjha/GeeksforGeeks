t=int(input())
for _ in range(t):
    n=int(input())
    k=n%10
    if(k<=5):
        print(n-k)
    else:
        res=10-k
        print(n+res)
