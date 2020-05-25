for _ in range(int(input())):
    n=int(input())
    arr=input().split()
    arr[i]=int(arr[i])+int(arr[int(arr[i])])%n*n
    for i in range(n):
        arr[i]=int(arr[i]/n)
    print(* arr)
        






    
