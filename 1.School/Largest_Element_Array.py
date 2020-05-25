t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=''
    ans=arr.sort()
    print(arr[-1])



