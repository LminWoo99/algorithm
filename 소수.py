n=int(input())

a=list()
for i in range(2, n):
    for x in range(2, i):
        if i%x==0:
            break
    else:
         a.append(i)   
    
print(len(a))