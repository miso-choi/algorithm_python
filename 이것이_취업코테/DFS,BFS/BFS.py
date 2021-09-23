# 큐 구현을 위해 deque 라이브러리 사용
from collections import deque

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


def BFS(graph,start,visited):
    queue = deque([start])  # 시작 노드를 담고있는 큐(deque)
    visited[start] = True   # 시작 노드 방문 처리
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소 하나씩 뽑아 출력
        v = queue.popleft()
        print(v,end=' ') # 옆으로 출력
        
        for i in graph[v]:   # 인접노드 중
            if not visited[i]:  # 방문 안한 노드
                queue.append(i)    # 큐에 삽입
                visited[i] = True  # 방문 처리
    
    


if __name__ == "__main__":
    # 예시 n, edge
    n = 8
    edge = [[1,2], [7,2],[6,7],[8,7],[1,8],[3,1],[3,4],[4,5],[3,5]]
    visited = [False]*(n+1)
    
    graph = MakeGraph(n,edge)
    BFS(graph,1,visited)  # 출력 결과: 1 2 7 6 8 3 4 5
