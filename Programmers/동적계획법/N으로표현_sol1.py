def solution(N, number):
    n_comb = []
    for _ in range(8):
        n_comb.append([-1])
    plus_comb = [0,0, [[1,2]], [[1,3],[2,2]],
                 [[1,4],[2,3]],  [[1,5],[2,4],[3,3]],  
                 [[1,6],[2,5],[3,4]],  [[1,7],[2,6],[3,5],[4,4]] ]
    rep = 0
    while(1):
        if rep == 0:
            n_comb[rep] = [N]

        elif rep == 1:
            temp_set = set()
            temp_set.add(N+N)
            temp_set.add(N*N)
            temp_set.add(N-N)
            temp_set.add(N//N)
            temp_set.add(int(str(N)*(rep+1)))
            n_comb[rep] = list(temp_set)

        else:
            temp_set = set()
            for pair in plus_comb[rep]:
                for n,f2 in enumerate(n_comb[pair[0]-1]):
                    for f1 in n_comb[pair[1]-1][n:]:
                        if f2 + f1 <= 32000:
                            temp_set.add(f2+f1)
                        if f2 * f1 <= 32000:
                            temp_set.add(f2*f1)
                        if f2 - f1 >= 1:
                            temp_set.add(f2-f1)
                        if f1 - f2 >= 1:
                            temp_set.add(f1-f2)
                        if (f1 != 0) and (f2 // f1 >= 1):
                            temp_set.add(f2//f1)
                        if (f2 != 0) and (f1 // f2 >= 1):
                            temp_set.add(f1//f2)
                        temp_set.add(int(str(N)*(rep+1)))        
            n_comb[rep] = list(temp_set)

        if (rep <= 7) & (number in n_comb[rep]):
            return rep+1
        elif rep == 7:
            return -1

        rep+=1