import heapq as hq

def solution(sc, K):
    hq.heapify(sc)
    ans = 0

    while (len(sc) > 1) & (sc[0] < K):
        ans += 1
        new = hq.heappop(sc) + 2*hq.heappop(sc)
        hq.heappush(sc,new)  
        
    if (len(sc) == 1) & (sc[0] < K):
        return -1
    elif(len(sc) >= 1) & (sc[0] >= K):
        return ans

