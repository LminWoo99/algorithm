a=list(range(21))
for i in range(10):
    b, c=map(int, input().split())
    for j in range((c-b+1)//2):
        a[b+j], a[c-j]= a[c-j], a[b+j]
a.pop(0)

print(a)