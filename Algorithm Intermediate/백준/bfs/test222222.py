from heapq import heappop, heappush
from collections import defaultdict
def solution(n, paths, gates, summits):
    def min_intensity():
        pq=[]
        visited=[10000001] * (n + 1)
        for gate in gates:
            heappush(pq, (0, gate))
            visited[gate]=0
        while pq:
            intensity, node=heappop(pq)
            if node in summits_set or intensity > visited[node]:
                continue
            for weight, next in mountain[node]:
                intensity=max(intensity, weight)
                if intensity < visited[next]:
                    visited[next]= intensity
                    heappush(pq, (intensity, next))
        intensity_min=[0, 10000001]
        for summit in summits:
            if visited[summit] < intensity_min[1]:
                intensity_min[0]= summit
                intensity_min[1]=visited[summit]
        return intensity_min
    summits.sort()
    summits_set = set(summits)
    mountain=defaultdict(list)
    for i,j,w in paths:
        mountain[i].append((w,j))
        mountain[j].append((w,i))
    return min_intensity()
        

        