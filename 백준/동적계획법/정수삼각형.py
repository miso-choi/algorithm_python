n = int(input())
num_list = []
d = [[] for _ in range(n)]

for _ in range(n):
    num_list.append(list(map(int,input().split())))

d[0].append(num_list[0][0])
for i in range(1,n):
    for cnt,j in enumerate(num_list[i]):
        if (cnt != 0) & (cnt != i):
            d[i].append(max(d[i-1][cnt-1]+j, d[i-1][cnt]+j))

        elif cnt == 0:
            d[i].append(d[i-1][cnt]+j)

        elif cnt == i:
            d[i].append(d[i-1][cnt-1]+j)
                
print(max(d[n-1]))