for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))

    l=0
    h=n-1
    while(l<h):
        while arr[l]==0 and l<h:
            l+=1
        while arr[h]==1 and l<h:
            h-=1


        if l<h:
            arr[l]=0
            arr[h]=1
            l+=1
            h-=1

    print(*arr)


            
