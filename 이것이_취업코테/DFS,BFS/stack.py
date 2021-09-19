# 스택(stack)은 list로 구현
stack = []

# 삽입은 append, 삭제는 pop 사용
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7) # 리스트의 뒤에 이어붙임
stack.pop()     # 후입선출
stack.append(1)
stack.append(4)
stack.pop()

# 최하단 원소부터 출력 (먼저 들어온 순)
print(stack)

# 최상단 원소부터 출력
print(stack[::-1])