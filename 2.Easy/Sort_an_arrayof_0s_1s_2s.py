def sort012(arr,n):
    l=0
    m=0
    h=n-1
    while(m<=h):
        if(arr[m]==0):
            arr[l],arr[m]=arr[m],arr[l]
            l+=1
            m+=1
        elif(arr[m]==1):
            m+=1
        elif(arr[m]==2):
            arr[m],arr[h]=arr[h],arr[m]
            h-=1
    

if __name__ == '__main__':
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int,input().split()))
        sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()
        
          
          
