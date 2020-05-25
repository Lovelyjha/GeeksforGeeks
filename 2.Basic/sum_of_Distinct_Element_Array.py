def SumofDistinctElement(arr,n):
    arr.sort()
    sum=arr[0]
    for i in range(n-1):
        if arr[i]!=arr[i+1]:
            sum+=arr[i+1]
    return sum


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(SumofDistinctElement(arr,n))
