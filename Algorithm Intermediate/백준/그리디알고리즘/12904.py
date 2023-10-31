import sys
input=sys.stdin.readline

s=input().rstrip()
t=input().rstrip()
i=0
while True:
    if s==t:
        print(1)
        break
    elif len(s)>len(t):
        print(0)
        break
    if t[-1]=='A':
        t=t[:-1]
    elif t[-1]=='B':
        t=t[:-1]
        t=t[::-1]
