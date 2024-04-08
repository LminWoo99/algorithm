import sys
input=sys.stdin.readline
from itertools import product

t=int(input())

modify=[' ', '+', '-']
for _ in range(t):
    res=[]
    n=int(input())
    a=[i for i in range(1, n+1)]
    for mod in product(modify, repeat=n-1):
        ans=str(a[0])
        for j in range(len(mod)):
            if mod[j]=='+' or mod[j]=='-':
                ans += mod[j]
            else:
                ans +=''
            ans+=str(a[j+1])
        check=eval(ans)
        
        if check==0:
            for k in range(len(mod)):
                print(a[k], end='')
                print(mod[k], end='')
            print(a[-1])
    print()


