def counting_sort(arr):
    count = [0]*(max(arr)+1)
    for a in arr:
        count[a] += 1

    for n, c in enumerate(count):
        for _ in range(c):
            print(n, end = ' ')

if __name__ == "__main__":
    arr = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
    counting_sort(arr)