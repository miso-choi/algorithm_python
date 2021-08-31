def solution(answers):
    std1 = 0; std2 = 0; std3 = 0
    for idx,ans in enumerate(answers):
        # 1번 수포자
        if (idx%5+1) == ans:
            std1 += 1
            
        # 2번 수포자
        if idx%2 == 0 and 2 == ans:
            std2 += 1
        elif idx%2 == 1:
            if idx%8 == 1 and ans == 1:
                std2 += 1
            elif idx%8 == 3 and ans == 3:
                std2 += 1
            elif idx%8 == 5 and ans == 4:
                std2 += 1
            elif idx%8 == 7 and ans == 5:
                std2 += 1
        
        # 3번 수포자
        if (idx%10 == 0 or idx%10 == 1) and (ans == 3):
            std3 += 1
        elif (idx%10 == 2 or idx%10 == 3) and (ans == 1):
            std3 += 1
        elif (idx%10 == 4 or idx%10 == 5) and (ans == 2):
            std3 += 1
        elif (idx%10 == 6 or idx%10 == 7) and (ans == 4):
            std3 += 1
        elif (idx%10 == 8 or idx%10 == 9) and (ans == 5):
            std3 += 1
    
    
    result = [std1,std2,std3]
    result_sorted = sorted(result, reverse=True)
    
    order_idx = list(map(lambda x: result.index(x),result_sorted))
    order_idx = list(map(lambda x: x+1,order_idx))
    
    if result_sorted[0] == result_sorted[1] == result_sorted[2]:
        return [1,2,3]
    
    elif result_sorted[1]==result_sorted[2]:
        return order_idx[0:1]
    
    elif result_sorted[0]==result_sorted[1]:
        temp = [order_idx[0],order_idx[2]]
        for i in [1,2,3]:
            if i not in temp:
                order_idx[1] = i
        return order_idx[0:2]
    
    if result_sorted[0] == result_sorted[1] == result_sorted[2]:
        return [1,2,3]
    
    else:
        return order_idx[0:1]
