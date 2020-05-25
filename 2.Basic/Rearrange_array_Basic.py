for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    b=arr[::-1]
    k=0
    p=0
    for i in range(n):
        if i%2==0:
            print(arr[k],end=' ')
            k+=1
        else:
            print(b[p],end=' ')
            p+=1
    print()

