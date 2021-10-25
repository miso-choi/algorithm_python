# Ch.3 성적이 낮은 순서로 학생 출력하기 (sol2-계수정렬)
def student_sort():
    N = int(input())
    std_list = [[] for _ in range(101)]

    for _ in range(N):
        std = input().split(' ')
        std[1] = int(std[1])
        std_list[std[1]].append(std[0])
        
    for st in std_list:
        if st != []:
            for s in st:
                print(s, end=' ')


if __name__ == "__main__":
    student_sort()