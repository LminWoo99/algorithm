n=int(input())
res=1
for i in range(n, 0, -1):
    res*=i
res=str(res)
res=res[::-1]
tmp=0
i=0
if res[0]!='0':
    print(0)
else:
    while True:
       if res[i]=='0':
            tmp+=1
            i+=1
       else:
           print(tmp)
           break
