def solution():
    N,K = map(int,input().split())
    cnt = 0
    while(N >= K):
        if N % K != 0:
            cnt += (N % K)
            N = N - (N % K)
        else:
            N = N / K
            cnt += 1
        
    if (1 < N < K):
        cnt += (N-1)
        # N = N - (N-1)
    
    return int(cnt)
