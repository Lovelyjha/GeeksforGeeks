t=int(input())
for _ in range(t):
    a=list(map(int,input().split()))
    for i in range(len(a)):
        if a[i]==a[i+1]:
            print(a[i])
            break
    
