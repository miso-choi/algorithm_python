def DFS(x,y):
    # frame 범위 벗어나면 종료
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    
    if frame[x][y] == 0:
        frame[x][y] = 1  # 방문처리 (0 -> 1)

        # 상, 하, 좌, 우 재귀적으로 호출 - 갈 수 있을 때까지 탐색
        DFS(x-1,y)
        DFS(x+1,y)
        DFS(x,y-1)
        DFS(x,y+1)
        return True # 0인 위치에서 시작해서 탐색 마침
    else:
        return False



if __name__ == "__main__":
    N,M = map(int,input().split())

    frame = []
    for _ in range(N):
        frame.append(list(map(int,input())))
    
    result = 0

    for n in range(N):
        for m in range(M):
            if DFS(n,m) == True:
              result += 1

    print(result)



'''
<입력 예시>
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

<출력 예시>
8
'''