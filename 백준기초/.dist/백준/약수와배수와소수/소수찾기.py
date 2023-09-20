n=int(input())
a=list(map(int, input().split()))
b=[]
for i in range(n):
    if n%(i+1)==0:
        b.append(i+1)
        if a[i]==len(b):
            print(a[i])