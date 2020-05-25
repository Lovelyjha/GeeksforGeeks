def DivideSubarray(arr,n):
    n=len(arr)
    ans=''
    sum1=0
    for i in range(int(n/2)):
        sum1+=arr[i]

    sum2=0
    i=int(n/2)
    while i<n:
        sum2+=arr[i]
        i+=1
    return abs(sum1*sum2)



t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(DivideSubarray(arr,n))
