def thirdLargest(arr, n):
    arr.sort()
    if len(arr)>=3:
        return arr[-3]
    else:
        return -1

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))


