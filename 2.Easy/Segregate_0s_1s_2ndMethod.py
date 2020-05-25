for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))

    l=0
    h=n-1
    while(l<h):
        if arr[l]==1:
            arr[l],arr[h]=arr[h],arr[l]
            h-=1
        else:
            l+=1
    print(*arr)
