def coin():
    N,M = map(int,input().split())

    coin_type = []

    for _ in range(N):
        coin_type.append(int(input()))

    coin_type.sort()  # 오름차순

    # 다이나믹 프로그래밍 진행 (Bottom-Up)
    d = [10001]*(M+1)
    d[0] = 0

    for coin in coin_type:
        for m in range(coin,M+1):
            d[m] = min(d[m],d[m-coin]+1)

    if d[m] == 10001:
        return -1
    else:
        return d[m]

    