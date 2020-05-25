def singleNumber(arr,n,k):
    return (k*sum(set(arr))-sum(arr))//(k-1)


t=int(input())
for _ in range(t):
    n,k=[int(n) for n in input().split()]
    arr=list(map(int,input().split()))
    print(singleNumber(arr,n,k))
    
