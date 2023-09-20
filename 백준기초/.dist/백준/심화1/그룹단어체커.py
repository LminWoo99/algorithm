n=int(input())
a=[]
res=n
for i in range(n):
    temp=input()
    if len(temp)!=1:
        for j in range(len(temp)-1):
            if temp[j]!=temp[j+1]:
                new_temp=temp[j+1:]
                if new_temp.find(temp[j])!=-1:
                    res-=1
                    break
print(res)