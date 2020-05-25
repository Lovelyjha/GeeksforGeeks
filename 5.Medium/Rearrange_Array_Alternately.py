def Rearrange(arrl,n):
    max=n-1
    min=0
    arr=[0 for i in range(n)]
    for i in range(n):
        if i%2!=0:
            arr[i]=arrl[min]
            min+=1
        else:
            arr[i]=arrl[max]
            max-=1
    for k in range(n):
        print(arr[k],end=" ")
    print()
        
            

for _ in range(int(input())):
    n=int(input())
    arrl=list(map(int,input().split()))
    Rearrange(arrl,n)
