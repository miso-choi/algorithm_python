def solution():
  N = int(input())
  x,y = 1,1
  order = input().split()

  # L,R,U,D에 따른 이동 방향
  dx = [0,0,-1,1]
  dy = [-1,1,0,0]
  move_types = ['L','R','U','D']

  # 이동 계획을 하나씩 확인
  for ord in order:
    # 이동 후 좌표 구하기
    for idx in range(len(move_types)):
      if ord == move_types[idx]:
        nx = x + dx[idx]
        ny = y + dy[idx]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > N or ny > N:
      continue
    # 이동 수행
    x,y = nx,ny
  print(x,y)
