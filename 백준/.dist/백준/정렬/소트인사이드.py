n=input()
a=[]
for i in range(len(n)):
    a.append(int(n[i]))
a.sort(reverse=True)
for i in a:
    print(i, end='')   
    