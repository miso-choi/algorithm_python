def solution(numbers, target):
    if (not numbers) and (target == 0) : # numbers가 비었을때 & target이 0일때 ->  target + (수의 조합) = 0  (OK)
        return 1
    elif (not numbers): # numbers가 비었을 때 & target이 0이 아닐때  ->   (No)
        return 0
    else:  # numbers가 비지 않았을 때 & (target은 상관 X) ->  더 깊이 들어가기  (Continue)
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
