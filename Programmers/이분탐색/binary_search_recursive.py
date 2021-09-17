def binary_search_recursive(target,arr,start,end):
  # arr는 오름차순 정렬되어있음을 가정함
  if end < start:
    print("arr에 찾고자 하는 target이 없습니다.")
    return None

  mid = (start + end) // 2
  if target == arr[mid]:
    print("arr의 인덱스 {0}번째에 target이 있습니다.".format(mid))
    return mid

  elif target < arr[mid]:
    return binary_search_recursive(target,arr,start,mid-1)

  else:   # target > arr[mid] 인 경우
    return binary_search_recursive(target,arr,mid+1,end)
  
  
if __name__ == "__main__":
  target = 2                # 테스트시 변경
  arr =[1,2,4,6,7,9,10]     # 테스트시 변경
  start = 0
  end = len(arr)-1
  answer = binary_search_recursive(target,arr,start,end)
  print(answer)
