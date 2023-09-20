import sys
input = sys.stdin.readline
n=int(input())
a=[]
for i in range(n):
    tmp=int(input())
    a.append(tmp)
a.sort()
for i in a:
    print(i)