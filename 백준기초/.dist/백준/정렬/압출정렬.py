import sys
input = sys.stdin.readline
n=int(input())
a=list(map(int, input().split()))
b=set(a)
newA=list(b)
newA.sort()
numDict={}
for i in range(len(newA)):
    numDict[newA[i]]=i
for i in a:
    print(numDict[i], end=' ')


