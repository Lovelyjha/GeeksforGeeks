t=int(input())
for _ in range(t):
    n=int(input())
    max_len = 0
    large = ''
    for i in range(n):
        s = input()
        if len(s) > max_len:
            max_len = len(s)
            large = s
    print(large)
    
