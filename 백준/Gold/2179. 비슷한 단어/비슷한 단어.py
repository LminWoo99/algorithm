import sys
input=sys.stdin.readline

n=int(input())
temp=[]
for _ in range(n):
    temp.append(input().rstrip())
wow=dict()
for idx,val in enumerate(temp):
    wow[val]=idx

a=temp[:]
a.sort()
res=0
res_len=[0]*(n+1)
for i in range(n-1):
    x,y=a[i], a[i+1]
    tmp=0
    j=0
    while j<len(x) and j<len(y):
        if x[j]==y[j]:
            tmp+=1
            j+=1
        else:
            break
    res=max(res, tmp)
    res_len[wow[x]]=max(res_len[wow[x]], tmp)
    res_len[wow[y]]=max(res_len[wow[y]], tmp)
prev=0
start=0
for i in range(n):
    if start==0:
        if res_len[i]==res:
            start=temp[i]
            print(start)
            prev=temp[i][:res]
    else:
        if res_len[i]==res and temp[i][:res]==prev: 
            print(temp[i])
            break