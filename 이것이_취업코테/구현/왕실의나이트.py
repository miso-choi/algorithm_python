def solution():
      loc = list(input())
  col = loc[0]
  row = loc[1]
  # 열 번호를 숫자(int)로 바꾸기
  col_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
  col = col_dict[col]
  
  # 행 번호를 int형으로 바꾸기
  row = int(row)
  
  cnt = 0
  steps = [(-1,-2),(1,-2),(-1,2),(1,2),(2,-1),(2,1),(-2,-1),(-2,1)]

  for step in steps:
    r = row + step[0]
    c = col + step[1]
    if (1 <= r <= 8) and (1 <= c <= 8): 
      cnt += 1

  return cnt