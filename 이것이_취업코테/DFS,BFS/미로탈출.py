from collections import deque

def BFS(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        X,Y = queue.popleft()

        for i in range(4):
            nx = X + dx[i]
            ny = Y + dy[i]
            
            ## 다음위치(nx,ny)가
            # 범위 벗어난 경우, 무시
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 벽인 경우, 무시
            if graph[nx][ny] == 0:
                continue
            
            ## 노드에 최단거리 기록 (처음 방문하는 경우에만)
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[X][Y] + 1
                queue.append((nx,ny))
    
    return graph[N-1][M-1]



if __name__ == "__main__":
    N,M = map(int,input().split())

    graph = []
    for _ in range(N):
        graph.append(list(map(int,input())))

    # (x,y):위치 index (x:행, y:열)
    # 이동할 네 방향 정의 (순서: 상,하,좌,우)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    print(BFS(0,0))


# 위치index (0,1)->(0,0)으로 거꾸로 가면서 (0,0)의 노드값이 3으로 업데이트 되긴 함.
# 그 뒤 탐색할 때 주변 노드중 1인 노드가 없어서 바로 종료됨.
'''
미로정보 입력 예시
110
010
011

graph 저장 방식
[[1,1,0], [0,1,0], [0,1,1]]

'''
    
    
    


