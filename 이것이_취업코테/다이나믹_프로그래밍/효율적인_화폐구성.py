def coin():
    N,M = map(int,input().split())

    coin_type = []
    count = 0

    for _ in range(N):
        coin_type.append(int(input()))

    coin_type.sort(reverse=True)


    for coin in coin_type:
        if M > coin:
            q = M // coin
            if q > 0:
                count += q
                M %= coin

    if M == 0:
        return count
    else:
        return -1
