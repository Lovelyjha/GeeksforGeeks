t=int(input())
for _ in range(t):
    n=input()
    count=0
    for i in n:
        if i.isupper():
            count+=1
    print(count)

        
        
