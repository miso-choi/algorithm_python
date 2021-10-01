# Bottom-Up 방식; 반복적
d = [0]*100

d[1] = 1
d[2] = 1
n = 99   # 구해야 하는 것: 피보나치 99번째 수

for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])