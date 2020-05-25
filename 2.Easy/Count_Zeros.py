def countZeros(arr,n):
    arr.sort(reverse=True)
    count=0
    for i in range(n):
        if arr[i]==0:
            count+=1
    return count
        

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(countZeros(arr,n))
    
