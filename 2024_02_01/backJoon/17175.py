N = int(input())

temp = [0 for _ in range(1000001)]

temp[0] = 0
temp[1] = 1

for i in range(2,N+1):

    temp[i] = (temp[i-1] + temp[i-2]) %1000000007

print(temp[N])