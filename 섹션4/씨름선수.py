n=int(input())
a=list()
for i in range(n):
    h, w=map(int, input().split())
    a.append((h,w))
a.sort(reverse=True)
lag=0
cnt=0
print(a)
for x,y in a:
    if y>lag:
        lag=y
        cnt+=1
print(cnt)
