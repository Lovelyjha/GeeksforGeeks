t=int(input())
for _ in range(t):
    a,b=input().split()
    if set(a)==set(b) and len(a)==len(b):
        print("YES")
    else:
        print("NO")
        
