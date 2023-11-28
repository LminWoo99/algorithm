from collections import defaultdict

def dfs(start, edges, visited):

    visited.add(start)
    vertex_count, edge_count = 1, 0  


    for edge in edges:
        if edge[0] == start:
            edge_count += 1
            if edge[1] not in visited:
                v_count, e_count = dfs(edge[1], edges, visited)
                vertex_count += v_count
                edge_count += e_count
    
    return vertex_count, edge_count

def solution(edges):
    in_edge = defaultdict(int)
    out = defaultdict(int)
    graph = {'donut': 0, 'bar': 0, 'eight': 0}
    

    for start, end in edges:
        out[start] += 1
        in_edge[end] += 1


    v = [node for node, out_degree in out.items() if out_degree > 1 and in_edge[node] == 0]
    if not v[0]:
        return [0, 0, 0, 0]  
    created_vertex = v[0]

    
    visited = set()
    vertex, line = dfs(created_vertex, edges, visited)
    

    if vertex == line:
        graph['donut'] += 1
    elif vertex == line + 1:
        graph['bar'] += 1
    elif vertex == line - 1:
        graph['eight'] += 1


    answer = [created_vertex, graph['donut'], graph['bar'], graph['eight']]
    return answer
