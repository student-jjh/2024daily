N = int(input())

temp_list= [0 for _ in range(1001)]
temp_list[1] =1
for i in range(2,N+1):
    if i % 2 == 0:
        temp_list[i] = (temp_list[i-1] * 2 +1) % 10007

    else:
        temp_list[i] = ((temp_list[i-1]-1) * 2 +1) % 10007

print(temp_list[N])



