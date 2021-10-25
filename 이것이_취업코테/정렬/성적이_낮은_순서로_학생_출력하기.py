# Ch.3 성적이 낮은 순서로 학생 출력하기
def student_sort():
    N = int(input())
    std_list = []

    for _ in range(N):
        std = input().split(' ')
        std[1] = int(std[1])
        std_list.append(std)
    std_list.sort(key = lambda x: x[1])

    print(list(map(lambda x: x[0], std_list)))

if __name__ == "__main__":
    student_sort()