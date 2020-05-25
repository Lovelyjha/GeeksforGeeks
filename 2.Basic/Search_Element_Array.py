t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    x=int(input())
    
    for i in range(n):
       if arr[i]==x:
           print(i)
           break
    else:
        print("-1")
        
