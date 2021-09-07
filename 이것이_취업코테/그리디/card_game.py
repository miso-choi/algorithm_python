def solution():
    N,M = map(int, input().split())
    card_total = []
    row_min = []
    for _ in range(N):
        card_total.append( list(map(int,input().split())) )

    for row in card_total:  # M번
        row_min.append(min(row))
    answer = max(row_min)

    return answer


def solution2():  # 공간복잡도 측면에서 더 좋은 풀이
    N,M = map(int, input().split())
    answer = 0
    for _ in range(N):
        data = list(map(int, input().split()))
        min_value = min(data)
        answer = max(answer, min_value)

    return answer