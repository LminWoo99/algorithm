n=[0]*31
for i in range(28):
    a=int(input())
    n[a]=1
for i in range(1,31):
    if n[i]==0:
        print(i)