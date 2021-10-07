n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

for i in range(1,n):
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1]) 

print(min(rgb[-1]))  # 가장 최하단 리스트 출력
