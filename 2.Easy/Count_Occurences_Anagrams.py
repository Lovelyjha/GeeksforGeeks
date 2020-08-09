t=int(input())
for _ in range(t):
    s=input()
    c=input()
    m=len(s)
    n=len(c)
    count=0
    st=sorted(c)
    for i in range(0,m-n+1):
        a=sorted(s[i:n+i])
        if(st==a):
            count+=1
    print(count)
        
