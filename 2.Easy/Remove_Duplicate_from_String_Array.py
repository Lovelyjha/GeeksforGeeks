def removeDuplicate(str,n):
    idx=0
    for i in range(0,n):
        for j in range(0,i+1):
            if str[i]==str[j]:
                break
        if j==i:
            str[idx]=str[i]
            idx+=1
    return "".join(str[:idx])

for _ in range(int(input())):
    str=input()
    n=len(str)
    print(removeDuplicate(list(str),n))
