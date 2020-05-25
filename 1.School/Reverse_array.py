n=int(input())
for i in range(n):
    s=int(input())
    l=list(map(int,input().split()))
    l.reverse()
    for j in l:
        print(j,end=' ')
    print()
