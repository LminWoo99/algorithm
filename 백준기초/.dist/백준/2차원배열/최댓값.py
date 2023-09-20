a=[]
for i in range(9):
    row=list(map(int, input().split()))
    a.append(row)
temp=0
x,y=0,0
for i in range(9):
    for j in range(9):
      if temp<a[i][j]:
          temp=a[i][j]
          x=i
          y=j
print(temp)
print(x+1, y+1)