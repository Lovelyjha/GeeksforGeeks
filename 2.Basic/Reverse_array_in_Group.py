def reverseInGroups(A,N,K):
    i=0
    while i<N:
        
        l=i
        r=min(i+K-1,N-1)
        while(l<r):
            A[l],A[r]=A[r],A[l]
            l+=1
            r-=1
        i+=K
    for i in range(0,N):
        
        return A
    

t=int(input())
for _ in range(t):
    N,K=[int(K) for K in input().split()]
    A=list(map(int,input().split()))
    print(reverseInGroups(A,N,K))
