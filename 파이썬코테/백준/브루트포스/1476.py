import sys
input=sys.stdin.readline
e,s,m=map(int, input().split())
cnt=1
a=1
b=1
c=1
while 1:
 
    if a==e and b==s and c==m:
        break
    a+=1
    b+=1
    c+=1
    cnt+=1
    if a>15:
        a=1
    if b>28:
        b=1   
    if c>19:
        c=1

print(cnt)    

    