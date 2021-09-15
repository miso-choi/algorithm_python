def sequential_search():
  print("생성할 원소 개수와 찾을 문자열을 한칸 띄고 입력하기:")
  n, target = input().split()
  n = int(n)
  print("앞에서 입력한 원소 개수만큼 문자열을 입력(띄어쓰기로 구분):")
  arr = input().split()

  for i in range(n):
    if arr[i] == target:
      return i    # target이 위치한 index 반환