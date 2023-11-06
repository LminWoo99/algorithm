import sys
input=sys.stdin.readline

n=int(input())
card={}


for i in range(n):
    tmp=int(input())
    if tmp in card:
        card[tmp] +=1
        continue
    card[tmp]=1
res=sorted(card.items(), key=lambda x:(-x[1], x[0]))
print(res[0][0])