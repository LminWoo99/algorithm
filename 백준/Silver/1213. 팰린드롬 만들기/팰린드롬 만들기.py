import sys
input=sys.stdin.readline
from collections import Counter

a=input().rstrip()
a=Counter(a)
cnt=0
mid=''
for target in a:
    if a[target]%2==1:
        mid=target
        cnt+=1
        if cnt>=2:
            print("I'm Sorry Hansoo")
            exit()
res=''
for target,cnt in sorted(a.items()):
    res+=(target*(cnt//2))
print(res+mid+res[::-1])