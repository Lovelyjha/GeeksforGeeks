def OddOccurrence(arr,n):
    res=0
    for i in arr:
        res=res ^ i

    return res
   

t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print("%d" %OddOccurrence(arr,n))
