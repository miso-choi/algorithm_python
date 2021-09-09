def solution():
  N = int(input())
  r = 1; c = 1
  order = list(input().split())
  for key in order:
    if (key == 'L') & (c != 1):
      c -= 1
    elif (key == 'R') & (c != N):
      c += 1
    elif (key == 'U') & (r != 1):
      r -= 1
    elif (key == 'D') & (r != N):
      r += 1
    
  print(r,c)

