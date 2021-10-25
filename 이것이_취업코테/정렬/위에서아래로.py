# Ch.2 위에서 아래로
def simple_sort():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    arr.sort(reverse = True)
    return arr


if __name__ == "__main__":
    arr = simple_sort()
    print(arr)