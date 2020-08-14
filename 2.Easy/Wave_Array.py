t=int(input())
for _ in range(t):
    n=int(input())
    a=input().split()
   
    for i in range(0,n-1,2):
            a[i],a[i+1]=a[i+1],a[i]
    print(*a)
