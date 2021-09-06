def solution(N):
    coin_list = [500,100,50,10]
    cnt = 0
    remain = N
    for coin in coin_list:
        cnt += remain // coin
        remain %= coin
    return cnt

# 시간복잡도
# coin_list의 원소개수가 K개라고 할 때, 시간복잡도는 O(K)이다.  
# 즉, 동전의 종류 개수(K)에만 영향을 받고, 거슬러 줘야하는 금액의 크기(N)과는 무관하다.