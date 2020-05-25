def CountPair(arr,n):
    result=0
    for i in range(n):
        for j in range(i+1,n):
            if(i*arr[i]>j*arr[j]):
                result+=1
            j=j+1
    return result


for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    print(CountPair(arr,n))
    
