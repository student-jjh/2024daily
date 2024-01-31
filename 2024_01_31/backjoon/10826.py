N = int(input())

temp_list = [0 for _ in range(10001)]

temp_list[1] = 1

for i in range(2,N+1):
    temp_list[i] = temp_list[i-1] +temp_list[i-2]
print(temp_list[N])