N = int(input())

temp = [0 for _ in range(117)]

temp[1] = 1
temp[2] = 1
temp[3] = 1

for i in range(4,N+1):
    temp[i] = temp[i-1] + temp[i-3]

print(temp[N])