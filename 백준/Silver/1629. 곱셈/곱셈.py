import sys
input=sys.stdin.readline
def solution(a, n):
    if n==1:
        return a %c
    else:
        tmp=solution(a, n//2)
        if n%2==0:
            return (tmp*tmp)%c
        else:
            return (tmp*tmp*a)%c
a,b,c=map(int, input().split())


print(solution(a,b))