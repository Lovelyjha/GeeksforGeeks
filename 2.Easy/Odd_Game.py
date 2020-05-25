def OddGame(n):
    for i in range(0,n):
        if(i%2==0):
            n.remove(i)
    remove n


for _ in range(int(input())):
    n=int(input())
    print(OddGame(n))
               
