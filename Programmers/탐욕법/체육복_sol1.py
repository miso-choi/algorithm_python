def solution(n, lost, reserve):
    lost_copy = lost.copy() ### for문에서 in 다음의 list원소를 중간에 remove하면 건너뛰게 되는 원소가 생기므로..
    for l in lost_copy:   
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)
    lost.sort()
    reserve.sort()

    for r in reserve:
        if r-1 in lost:
            lost.remove(r-1)
            
        elif r+1 in lost:
            lost.remove(r+1)
            
    return n - len(lost)
    
