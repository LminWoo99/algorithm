from collections import defaultdict
def solution(tickets):
    graph=defaultdict(list)
    n=len(tickets)
    visit=[0]*n
    answer=[]
    def DFS(cur_airport, path):
        if len(path)==n+1:
            answer.append(path)
            return
        for idx,val in enumerate(tickets):
            if val[0]==cur_airport and not visit[idx]:
                visit[idx]=1
                DFS(val[1], path+[val[1]])
                visit[idx]=0
    DFS("ICN",["ICN"])
    answer.sort()
    return answer[0]