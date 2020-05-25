def Minimum_Cost(arr,n):
    return (n-1)*min(arr)

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(Minimum_Cost(arr,n))
    
    
