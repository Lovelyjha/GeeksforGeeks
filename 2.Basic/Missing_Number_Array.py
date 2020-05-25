def OddOccurrence(arr,n):
    s=sum(arr)
    s1=sum(range(1,n+1))
    return s1-s
    
    


t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    print(OddOccurrence(arr,n))
