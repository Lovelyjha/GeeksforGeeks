def printAl(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
        i+=2

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        print(printAl(arr,n))
