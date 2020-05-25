t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))

    x=arr[n-1]
    for i in range(n-1,0,-1):
        arr[i]=arr[i-1]
    arr[0]=x
    print(*arr)
