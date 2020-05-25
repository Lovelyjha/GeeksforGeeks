for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))


    for i in range(n):
        count=0
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1
        if count%2!=0:
            break
    print(arr[i])
