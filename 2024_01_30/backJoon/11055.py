N = int(input())

temp_list = list(map(int,input().split()))

d = [x for x in temp_list]
d[0] = temp_list[0]

for i in range(0,N):
    for j in range(i,N):
        if temp_list[j] > temp_list[i] and d[j] < d[i] + temp_list[j]:
            d[j] = d[i] + temp_list[j]

print(max(d))
