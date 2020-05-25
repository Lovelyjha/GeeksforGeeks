def isPrime(num):
    i=2
    flag=True
    while i<=int(num//2):
        if num%i==0:
            flag=False
            break
        i+=1
    return flag
for _ in range(int(input())):
    num=int(input())
    for n in range(2,num):
        if isPrime(n)==True and isPrime(num-n)==True:
            print(n,(num-n))
            break
