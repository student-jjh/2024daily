N = int(input())

temp = list(map(int,input().split()))
for_print = [-1 for _ in range(N)]
not_found = [0]

i = 1
while not_found and i < N:
    while not_found and temp[not_found[-1]] < temp[i]:
        for_print[not_found.pop()] = temp[i]

    not_found.append(i)
    i+=1

for item in for_print:
    print(item,end = " ")

