
def solution(info, edges):
    answer = 0
    n=len(info)
    graphs=[[] for _ in range(n)]
    for edge in edges:
        graphs[edge[0]].append(edge[1])
        graphs[edge[1]].append(edge[0])
    visit=[0]*(n)
    
    def DFS(start,L,n,visit, sheep, wolf):
        print(L)
        if L==n-1:
            print("wow")
            if sheep>wolf:

                answer=max(answer,sheep)
            return 
        if wolf>=sheep:
            return
        for graph in graphs[start]:
            if not info[graph]:
                if not visit[graph]:
                    visit[graph]=1
                    DFS(graph, L+1, n,visit, sheep+1, wolf)
                    visit[graph]=0
            else:
                if not visit[graph]:
                    visit[graph]=1
                    DFS(graph, L+1, n,visit, sheep, wolf+1)
                    visit[graph]=0
    DFS(0,1,n,visit, 1,0)
            
    return answer
solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]])