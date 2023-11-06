import sys
input=sys.stdin.readline

n=int(input())
score=[]
for i in range(n):
    name, korea, english, math= map(str, input().rstrip().split())
    korea,english, math=int(korea), int(english), int(math)
    score.append((name,korea, english, math))
score=sorted(score, key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in range(n):
    print(score[i][0])
                        