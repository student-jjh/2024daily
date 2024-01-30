N = int(input())

temp_list = list(map(int,input().split()))

d = [1 for x in temp_list]


for i in range(0,N):
    for j in range(i,N):
        if temp_list[j] > temp_list[i] and d[j] < d[i] + 1:
            d[j] = d[i] + 1

print(max(d))
