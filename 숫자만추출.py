n=input()
temp=''
res=0
j=2
for i in range(len(n)):

    if ord(n[i])<57:
        temp+=n[i]
temp=int(temp)
print(temp)
for j in range(1, temp+1):
    if temp%j==0:
        res+=1
print(res)
    