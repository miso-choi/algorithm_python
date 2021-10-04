n = int(input())

arr = list(map(int, input().split()))

# DP 테이블 초기화
d = [0]*100

# Bottom-Up DP 진행
d[0] = arr[0]
d[1] = max(arr[0],arr[1])

# 왼쪽에서부터 식량 털음. 
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2]+arr[i])

# arr 전체 (idx:0부터 n-1까지) 다 살펴본 결과, 최대 식량 수
print(d[n-1]) 
