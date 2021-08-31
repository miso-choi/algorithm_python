def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    lesser_arr, equal_arr, greater_arr = [], [], []
    quick = arr[len(arr)//2] #몫
    for num in arr:
        if num < quick:
            lesser_arr.append(num)
        elif num > quick:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)    

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        split_arr = []
        start = commands[i][0]-1
        end = commands[i][1]-1
        for j in range(end - start + 1):
            split_arr.append(array[start+j])
        sorted_arr = quick_sort(split_arr)
        answer.append(sorted_arr[commands[i][2]-1])

    return answer