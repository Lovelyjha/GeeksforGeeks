def Min_Sum_formed(arr,n):
    arr.sort()
    a=0
    b=0
    for i in range(n):
        if i%2!=0:
            a=a*10+arr[i]
        else:
            b=b*10+arr[i]
    return a+b
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(Min_Sum_formed(arr,n))
