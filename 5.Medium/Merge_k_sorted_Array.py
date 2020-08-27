#Given K sorted arrays arranged in the form of a matrix of size K*K.
#The task is to merge them into one sorted array


t=int(input())
for _ in range(n):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    li=[]
    for i in range(n):
        li+=arr[i]
        li.sort()
    return li



