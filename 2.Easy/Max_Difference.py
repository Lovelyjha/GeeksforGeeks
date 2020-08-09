t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    max_diff=a[0]-a[1]
    min_ele=a[0]
    for i in range(n):
        if a[i]-min_ele > max_diff:
            max_diff=a[i]-min_ele
        if a[i]<min_ele:
            min_ele=a[i]
    print(max_diff)
        
        
        
