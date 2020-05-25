for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(0,n):
        if arr[i]!=i and arr[i]!=-1:
            x=arr[i]

            while(arr[x]!=-1 and arr[x]!=x):
                y=arr[x]
                arr[x]=x
                x=y
            arr[x]=x
            if(arr[i]!=i):
               arr[i]=-1
    print(*arr)
            
