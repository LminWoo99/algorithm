n=int(input())
meet=list()
for i in range(n):
    a,b=map(int, input().split())
    meet.append((a,b))
    meet.sort(key=lambda x : (x[1], x[0]))
et=0
cnt=0
for s,e in meet:
    if s>=et:
        et=e
        cnt+=1
print(cnt)