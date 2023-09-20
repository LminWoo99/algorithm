n=int(input())
df=[0]*100
df[0]=1
df[1]=1
df[2]=1
df[3]=2
df[4]=2
for i in range(n):
    tmp=int(input())
    for j in range(5, tmp):
      df[j]=df[j-1]+df[j-5]
    print(df[tmp-1])


