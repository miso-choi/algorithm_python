def solution():
    N,M,K = map(int,input().split())
    arr = list(map(int,input().split()))
    
    q = M // (K+1)
    r = M % (K+1)
    
    total = max(arr)*(K*q + r) 

    arr.remove(max(arr))
    total += max(arr)*q
    return total

# 시간복잡도
# max, remove는 O(N), 나머지,몫 연산은 O(1)  =>  결과적으로, O(N)