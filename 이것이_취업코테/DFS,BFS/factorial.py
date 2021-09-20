# 반복적으로 구현한 n!
def factorial_iterative(n):
  result = 1
  for i in range(1,n+1):
    result *= i
  return result


# 재귀적으로 구현한 n!
def factorial_recursive(n):
  # n은 0이상의 정수만 받음
  if n <= 1:
    return 1
  return n*factorial_recursive(n-1)
