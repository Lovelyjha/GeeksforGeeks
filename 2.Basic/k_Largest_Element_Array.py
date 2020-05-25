def k_largest(num,inp2):
    lis=[]
    inp2.sort()
    inp2.reverse()
    for i in range(num):
        lis.append(inp2[i])
    print(*lis)

t=int(input())
for i in range(t):
    inp1=[int(y) for y in input().strip().split()]
    inp2=[int(x) for x in input().strip().split()]
    k_largest(inp1[1],inp2)

-----------------xxxxxxxx-----------------

for _ in range(int(input())):
n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr, reverse = True)
print(*arr[:k])
