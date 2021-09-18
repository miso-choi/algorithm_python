def solution(n,times):
    times.sort()
    start = 1
    end = times[-1]*n   # 심사시간 최악의 경우
    
    answer = 0

    while(start <= end):
        # 심사하는데 걸린 시간이 mid 라면,
        mid = (start + end) // 2

        # 그 mid 시간동안 people명을 심사했을 것
        people = 0
        for t in times:
            people += mid // t
            if people >= n:  # 중간에라도 people이 n보다 커지면 탈출
                break
        
        if n <= people:
            # mid 시간동안 n명보다 크거나 같은 사람들(people)을 심사했다니
            # 그렇다면 n명을 심사하기 위해선 시간을 더 줄일 수 있겠구나.
            
            answer = mid # mid시간동안 적어도 n명은 심사 가능하다는 것이므로 여기서 저장!

            end = mid - 1

        else:   # n > people
            start = mid + 1
    return answer



## n == people이 됐을 때 while문 어떻게 탈출하는가?
## -> 우선 if에 걸리니 end = mid - 1 해준다. 다음에는 바로 while문 조건에 걸리거나, else로 가서 start = mid+1 해준 뒤 while문 조건에 걸려서 탈출함.
  
      
## n == people인 경우 말고도, 왜 n < people인 경우까지 포함해서 answer = mid를 하여 저장하는가??
## -> 예시) n:9, times:[3,5,2]의 경우, 심사시간 10분동안 10명까지 가능한게 맞지만, 문제에서 9명을 심사하는데 걸리는 시간 구하라 했으니. 9명도 10분인건 똑같아서..
