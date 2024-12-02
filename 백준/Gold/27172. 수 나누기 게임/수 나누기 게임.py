import sys
from collections import defaultdict
input=sys.stdin.readline
## 최대 nlogn
n=int(input())
cards=list(map(int, input().split()))
# 1 3 9 12
# 3 1 -2 -2

score=defaultdict(int)
for i in range(n):
    score[cards[i]]=0
cards=set(cards)
max_card=max(cards)
for card in cards:
    if card==max_card:
        continue
    for i in range(2*card, max_card+1, card):
        if i in cards:
            score[card]+=1
            score[i]-=1

print(*list(score.values()))