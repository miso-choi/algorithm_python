# Top-Down 방식; 재귀적
d = [0]*100

def fibo(n):
    # 호출되는 함수 확인
    print("f("+str(n)+")")

    # n이 1 또는 2일 때
    if n == 1 or n == 2:
        return 1
    
    # fibo(n)이 이미 계산된 값이면 그대로 반환
    if d[n] != 0:
        return d[n]
    
    else:
        # 아직 계산하지 않은 값이면 점화식에 따라 피보나치 결과 반환
        d[n] = fibo(n-1) + fibo(n-2)
        return d[n]

print(fibo(6))