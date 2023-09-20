a=[]
b=''
for i in range(5):
    row=input()
    a.append(row)
for j in range(15):
    for i in range(5):
        if j < len(a[i]):
            print(a[i][j], end='')