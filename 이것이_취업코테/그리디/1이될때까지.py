def solution():
  N,K = map(int,input().split())
  cnt = 0
  while(1):
    if N % K != 0:
      N = N-(N % K)
      cnt = cnt + N % K
    else:
      N = N / K

    if N == 1:
      break
  return cnt