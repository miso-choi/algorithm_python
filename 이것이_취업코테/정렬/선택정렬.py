import time 

def selection_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        min_idx = i
        for j in range(i+1,arr_len):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # arr의 인덱스 i와 min_idx 원소를 swap
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


if __name__ == "__main__":
    start = time.time()
    arr = selection_sort([7,5,9,0,3,1,6,2,4,8])
    print("걸린 시간:", time.time()-start)  # 1.407e-05 정도
    print(arr)