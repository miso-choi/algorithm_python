import time

def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j-1] <= arr[j]:
                break
            else:
                arr[j-1], arr[j] = arr[j], arr[j-1]
    return arr

if __name__ == "__main__":
    start = time.time()
    arr = [7,5,9,0,3,1,6,2,4,8]
    arr = insertion_sort(arr)
    print(arr)
    print("걸린시간:", time.time()-start) # 5.913e-05 정도