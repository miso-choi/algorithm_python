import time

def quick_sort(arr):
    # 재귀함수 종료조건
    if len(arr) <= 1:
        return arr
    pivot = 0
    left = 1
    right = len(arr)-1

    while left <= right:
        # 왼쪽부터 하나씩 탐색 (피벗보다 큰 수 나올때까지)
        while left <= len(arr)-1 and arr[left] <= arr[pivot]:
            left += 1

        # 오른쪽부터 하나씩 탐색 (피벗보다 작은 수 나올때까지)
        while right > 0 and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]

        else:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr_left = arr[:right]
    arr_right = arr[right+1:]

    return quick_sort(arr_left) + [pivot] + quick_sort(arr_right)
    

if __name__ == "__main__":
    start = time.time()
    arr = [5,4,9,0,3,1,6,2,7,8]
    sorted_arr = quick_sort(arr)
    print(sorted_arr)
    print("걸린 시간:", time.time()-start)
    print(arr)
