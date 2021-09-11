def solution():
    N = int(input())

    count = 0
    for hour in range(N+1):
        for min in range(60):
            for sec in range(60):
                if '3' in str(hour)+str(min)+str(sec):
                    count += 1
    return count
