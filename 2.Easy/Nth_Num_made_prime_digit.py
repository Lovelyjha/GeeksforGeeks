def nthprimtdigitsnumber(n):
    num=""
    while(n>0):
        rem=n%4
        if rem==1:
            num+='2'
        if rem==2:
            num+='3'
        if rem==3:
            num+='5'
        if rem==0:
            n=n-1
            num+='7'
        n=n//4
    return num[::-1]
t=int(input())
for _ in range(t):
    n=int(input())
    print(nthprimtdigitsnumber(n))
