# 평범한 배낭 (0-1 배낭문제)
N,K = map(int,input().split())
info = [list(map(int,input().split())) for _ in range(N)]
arr = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for s in range(1,K+1):
        if info[i-1][0] > s:
            arr[i][s] = arr[i-1][s]
        else:
            arr[i][s] = max(info[i-1][1] + arr[i-1][s-info[i-1][0]], arr[i-1][s])
                
print(arr[N][K])

# Python3로 채점시 통과되긴 하지만 시간이 오래걸림 -> 똑같은 코드 Pypy3로 실행시 훨씬 빠름 
