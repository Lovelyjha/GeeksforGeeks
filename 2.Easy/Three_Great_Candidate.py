def maxProduct(arr,n):
    if n<3:
        return -1
    arr.sort()
    return max(arr[0]*arr[1]*arr[n-1],arr[n-1]*arr[n-2]*arr[n-3])
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(maxProduct(arr,n))
