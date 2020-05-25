t=int(input())
while t>0:
    t=t-1
    n = int(input())
    s=input().split(" ")
    arr=[]
    for i in range(0,n):
        arr.append(int(s[i]))
    printed=False
    for i in range(0,n-1):
        if arr[i]>arr[i+1]:
            print(arr[i])
            printed=True
            break
    if not printed:
        print(arr[n-1])
