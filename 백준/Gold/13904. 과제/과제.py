import sys, heapq
input=sys.stdin.readline

n=int(input())
subject_list=[] # 과제 리스트
tmp=0
for _ in range(n):
    d,w=map(int, input().split()) #과제 마감일까지 남은 일수, 과제의 점수
    heapq.heappush(subject_list, (-w,d))
    tmp=max(d, tmp)
visit=[False]*(tmp+1) # 지정
ans=0
while subject_list:
    score, restDay=heapq.heappop(subject_list)
    score=-score
    for i in range(restDay, 0, -1):
        if not visit[i]:
            visit[i]=True
            ans+=score
            break
print(ans)