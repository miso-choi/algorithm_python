import time

def quick_sort(arr):
    # 재귀함수 종료조건
    if len(arr) <= 1:
        return arr
   
    pivot = arr[0]
    tail = arr[1:]
    
    arr_left = [x for x in tail if x <= pivot]
    arr_right = [x for x in tail if x > pivot]

    return quick_sort(arr_left) + [pivot] + quick_sort(arr_right)
    

if __name__ == "__main__":
    start = time.time()
    arr = [5,4,9,0,3,1,6,2,7,8]
    sorted_arr = quick_sort(arr)
    print(sorted_arr)
    print("걸린 시간:", time.time()-start)