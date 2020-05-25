t=int(input())
for _ in range(t):
    num1,num2=list(map(int,input().split()))
    ans=num1%num2
    print(ans)
