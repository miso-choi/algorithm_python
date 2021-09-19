from collections import deque
# 큐(queue) 구현을 위해 deque 라이브러리 사용
# deque : 데이터를 넣고 빼는 속도가 list 자료형에 비해 효율적임
queue = deque()

# 삽입(5)-삽입(2)-삽입(3)-삽입(7)-삭제()-삽입(1)-삽입(4)-삭제()
# 삽입은 append(), 삭제는 popleft() 사용
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)  # 뒤에 이어붙임 - 스택과 동일
queue.popleft()  # 선입선출(FIFO)
queue.append(1)
queue.append(4)
queue.popleft()


# 먼저 들어온 순 출력
print(queue)

# 역순 출력
queue.reverse()# 다음 출력을 위해 reverse (default: inplace=True)
print(queue)
# 리스트 자료형으로 변경
print(list(queue))