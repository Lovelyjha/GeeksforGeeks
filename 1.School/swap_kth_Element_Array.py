t=int(input())
for _ in range(t):
    n,k=[int(n) for n in input().split()]
    arr=list(map(int,input().split()))

    
    for i in range(n):
        temp=arr[k-1]
        arr[k-1]=arr[n-k]
        arr[n-k]=temp
        break
    print(*arr)
    
