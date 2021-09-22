def MakeGraph(n, edge):
    # graph 인접리스트 생성시, index 0 자리는 버림
    # 편의를 위해 node 1의 인접노드 정보를 index 1에 저장
    graph = [set() for _ in range(n+1)]
    
    for e in edge:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])

    graph = list(map(list,graph))
    
    print("graph :",graph)
    return graph


def DFS(graph,v,visited):
    visited[v] = True
    print(v,end=' ') # 옆으로 출력
    for i in graph[v]:
        if not visited[i]:
            DFS(graph,i,visited)


if __name__ == "__main__":
    # 예시 n, edge
    n = 8
    edge = [[1,2], [7,2],[6,7],[8,7],[1,8],[3,1],[3,4],[4,5],[3,5]]
    visited = [False]*(n+1)
    
    graph = MakeGraph(n,edge)
    DFS(graph,1,visited)
