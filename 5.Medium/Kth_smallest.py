def kthSmallest(arr,n,k):
    arr.sort()
    return arr[k-1]
t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    print(kthSmallest(arr,n,k))
