b=list()

n=int(input())
a=list(map(int, input().split()))
def digit_sum(x):
   num=0
   for i in str(x):
       num+=int(i)
   return num
max=0
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)     
    





