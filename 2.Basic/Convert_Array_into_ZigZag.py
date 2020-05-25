t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    flag=True
    for i in range(n-1):
        if flag is True:
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        else:
            if arr[i]<arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
        flag=bool(1-flag)
    print(* arr)
            
        



    
