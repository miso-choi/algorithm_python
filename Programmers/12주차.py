from itertools import permutations
def solution(k, dungeons):  
    # 각 원소의 index 0이 k 이하인 것들만 filtering
    new_d = []
    for d in dungeons:
        if d[0] <= k:
            new_d.append(d)
    
    # 1부터 던젼 개수 n까지의 리스트 생성
    num = [i for i in range(0,len(dungeons))]
    
    # 모든 순서 경우 리스트를 순열로 생성 후, 완전탐색하여 최대 count 찾기
    max_value = 0
    for order in list(permutations(num)):
        k_cp = k
        count = 0
        for i in order:
            if k_cp > 0:
                if k_cp >= new_d[i][0]:
                    k_cp -= new_d[i][1]
                    count += 1
            else:
                break
        max_value = max(max_value, count)
    
    return max_value


if __name__ == "__main__":
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    result = solution(k,dungeons)
    print(result)