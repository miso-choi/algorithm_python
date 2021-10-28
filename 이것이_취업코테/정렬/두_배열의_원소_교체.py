def solution():
    N,K = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort(reverse = True)

    for i in range(K):
        if A[i] < B[i]:
            A[i],B[i] = B[i],A[i]
        else:  
            break   # 정렬했기 때문에 A[i] >= B[i]이면 종료

    return sum(A)  # 기본 라이브러리 사용

if __name__ == "__main__":
    result = solution()
    print(result)
        
