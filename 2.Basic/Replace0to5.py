def convert0to5(num):
   ans=0
   p=1
   while(num>0):
       digit=num%10
       if digit==0:
           digit=5
       ans+=p*digit
       num=num//10
       p=p*10
   return ans
t=int(input())
for _ in range(t):
    num=int(input())
    print(convert0to5(num))
