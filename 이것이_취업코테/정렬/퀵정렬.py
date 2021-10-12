import time

def quick_sort(arr,start,end):
    # 재귀함수 종료조건
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 왼쪽부터 하나씩 탐색 (피벗보다 큰 수 나올때까지)
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # 오른쪽부터 하나씩 탐색 (피벗보다 작은 수 나올때까지)
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]

        else:
            arr[left], arr[right] = arr[right], arr[left]
        
    quick_sort(arr,start,right-1)
    quick_sort(arr,right+1,end)
    

if __name__ == "__main__":
    start = time.time()
    arr = [5,4,9,0,3,1,6,2,7,8]
    quick_sort(arr,0,len(arr)-1)
    print("걸린 시간:", time.time()-start)
    print(arr)