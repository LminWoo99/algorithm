import sys
import math
input=sys.stdin.readline
def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False 
    return True 

n=int(input())
cand=[]
if n>=2:
    cand.append(2)
for i in range(3, n+1):
    if i%2!=0:
        if is_prime_number(i):
            cand.append(i)
left,right=0,0
cnt=0
cur_sum=0
while True:
    if cur_sum>=n:
        if cur_sum==n:
            cnt+=1
        cur_sum-=cand[left]
        left+=1
    elif right==len(cand):
        break
    else:
        cur_sum+=cand[right]
        right+=1
print(cnt)
        
