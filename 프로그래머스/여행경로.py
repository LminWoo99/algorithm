def solution(tickets):
    answer = []
    
    visited = [False]*len(tickets)
    
    def DFS(airport, path):
        if len(path)==len(tickets)+1:
            answer.append(path)
            return
        print(path)
        for idx, ticket in enumerate(tickets):
            if airport==ticket[0] and not visited[idx]:
                visited[idx]=True
                DFS(ticket[1], path+[ticket[1]])
                visited[idx]=False
        
        
        
    DFS("ICN", ["ICN"])
    
    answer.sort()

    return answer[0]