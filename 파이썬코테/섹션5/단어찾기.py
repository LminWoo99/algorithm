n=int(input())
p=dict()
for i in range(n):
    word=input()
    p[word]=1
for i in range(n-1):
    word=input()
    p[word]=0
print(p)
for key, val in p.items():
    if val==1:
        print(key)
        break