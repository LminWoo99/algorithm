import sys
input=sys.stdin.readline

n=int(input())
positive=[]
negative=[]
max_sum=0
for i in range(n):
    tmp=int(input())
    if tmp>1:
        positive.append(tmp)
    elif tmp ==1:
        max_sum+=1
    else:
        negative.append(tmp)
positive.sort(reverse=True)
negative.sort()
    
if len(positive) % 2 ==0:
    for i in range(0, len(positive), 2):
        max_sum+= positive[i]*positive[i+1]
else:
    for i in range(0, len(positive)-1 , 2):
        max_sum += positive[i] * positive[i+1]
    max_sum += positive[len(positive)-1]
if len(negative) % 2 ==0:
    for i in range(0, len(negative), 2):
        max_sum += negative[i] * negative[i+1]
else:
     for i in range(0, len(negative)-1, 2):
          max_sum += negative[i] * negative[i+1]
     max_sum += negative[len(negative)-1] 
     
print(max_sum)
