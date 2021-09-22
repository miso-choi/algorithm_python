def MakeGraph(n, edge):
    # graph 인접리스트 생성시, index 0 자리는 버림
    # 편의를 위해 node 1의 인접노드 정보를 index 1에 저장
    graph = [[] for _ in range(n+1)]
    
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    # 일반적으로 인접한 노드 중 방문하지 않은 노드가 여러 개 있으면 번호 낮은 순서대로 처리 
    # -> 각 인접리스트 오름차순 정렬
    graph = list(map(lambda x: sorted(x), graph))

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
    DFS(graph,1,visited)  # 출력 결과: 1 2 7 6 8 3 4 5
