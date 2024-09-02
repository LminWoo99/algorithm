from collections import defaultdict
import heapq
def solution(n, paths, gates, summits):
    summits.sort()
    summits_set=set(summits)
    mountain=defaultdict(list)
    for i,j,w in paths:
        mountain[i].append((w,j))
        mountain[j].append((w,i))
    
    def min_intensity():
        hq=[]
        visit=[10000001] * (n + 1)
        for gate in gates:
            visit[gate]=0
            heapq.heappush(hq, (0,gate))
        while hq:
            cnt, x=heapq.heappop(hq)
            if x in summits_set or cnt>visit[x]:
                continue
            for next_cnt,next_node in mountain[x]:
                new_cnt=max(next_cnt, cnt)
                if new_cnt<visit[next_node]:
                    visit[next_node]=new_cnt
                    heapq.heappush(hq, (new_cnt, next_node))
        a=[0, 10000001]
        for summit in summits:
            if visit[summit]<a[1]:
                a[0]=summit
                a[1]=visit[summit]
        return a
            
    return min_intensity()
        

        