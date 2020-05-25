for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    max_right=arr[n-1]
    arr[n-1]=-1
    for i in range(n-2,-1,-1):
        temp=arr[i]
        arr[i]=max_right

        if max_right<temp:
            max_right=temp
    print(*arr)
