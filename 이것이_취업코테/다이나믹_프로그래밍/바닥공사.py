N = int(input()) # 가로 길이


# DP 테이블 초기화
# 각 index : N이 그 값일 때 가능한 방법의 수
d = [0]*1001

# d[0]: 사용X
d[1] = 1
d[2] = 3

for i in range(3,N+1):
    d[i] = (d[i-1] + 2*d[i-2]) % 796796

print(d[N])    
