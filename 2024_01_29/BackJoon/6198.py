N = int(input())

temp = []
for i in range(N):
    temp.append(int(input()))
for_print = [-1 for _ in range(N)]
not_found = [0]

i = 1
while not_found and i < N:
    while not_found and temp[not_found[-1]] <= temp[i]:
        for_print[not_found.pop()] = i

    not_found.append(i)
    i+=1



answer = 0
for i in range(len(for_print)):
    if for_print[i] != -1:
        answer += for_print[i] - i -1

    elif for_print[i] ==-1:
        answer += N - i -1

print(answer)


