import sys
import copy
input=sys.stdin.readline

n,m=map(int, input().split())
a=[list(input().rstrip()) for _ in range(n)]



res=[]
for x in range(n-7):
    for y in range(m-7):
        black=0
        white=0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i+j)%2==0:
                    if a[i][j]!='B':
                        black+=1
                    if a[i][j]!='W':
                        white+=1
                else:
                    if a[i][j]!='W':
                        black+=1
                    if a[i][j]!='B':
                        white+=1
        res.append(black)                
        res.append(white)                

                        
print(min(res))
            

