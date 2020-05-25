def FunNum(arr,n,k):
    count=0
    for i in range(n):
        temp=arr[i]
        while(temp>0):
            if temp%10==k:
                count+=1
            temp//=10
    return count
    

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    print(FunNum(arr,n,k))
    
