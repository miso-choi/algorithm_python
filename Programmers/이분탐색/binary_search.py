def binary_search(target,arr):
  # arr는 오름차순 정렬되어있음을 가정함
  start = 0
  end = len(arr)-1
  while(start <= end):
    mid = (start + end) // 2
    if target == arr[mid]:
      print("arr의 인덱스 {0}번째에 target이 있습니다.".format(mid))
      return mid

    elif target < arr[mid]:
      end = mid - 1

    else:   # target > arr[mid] 인 경우
      start = mid + 1
  
  print("arr에 찾고자 하는 target이 없습니다.")
  return None
