import sys
input=sys.stdin.readline

s=input().rstrip()
T=input().rstrip()
def dfs(t):
    if s==t:
        print(1)
        sys.exit()
    if len(t)==0:
        return 0
    if t[-1]=='A':
        dfs(t[:-1])
    if t[0]=='B':
        dfs(t[1:][::-1])
dfs(T)
print(0)

