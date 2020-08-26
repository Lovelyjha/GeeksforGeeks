def countSubarrWithEqualZeroAndOne(arr, N):
    for i in range(N):
        if arr[i]==0:
            arr[i]=-1  #Replace all 0 with -1
    dict={}
    sum=0
    count=0
    for i in range(N):
        sum+=arr[i]     #Now sum=0 then add value of array to the n
        if sum==0:      #if sum=0 then current_index+1
            count+=1
        if sum not in dict:
            dict[sum]=1
        else:
            count+=dict[sum]
            dict[sum]+=1
            
            
    return count

t=int(input())
for _ in range(t):
    N=int(input())
    arr=list(map(int,input().split()))
    print(countSubarrWithEqualZeroAndOne(arr, N))
    
