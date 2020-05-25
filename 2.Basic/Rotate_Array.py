def Rotate_array(arr,n,d):
    for i in range(d):
        temp=arr[0]
        for j in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp
    return arr[i]
        

arr=eval(input())
n=int(input())
d=list(map(int,input().split()))
print(Rotate_array(arr,n,d))
        
