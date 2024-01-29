N = int(input())

listOfTower = list(map(int,input().split()))
for_answer = [0 for _ in range(N)]
not_found = [N-1]
i = N-1


while not_found and i >= 0:
    while not_found and listOfTower[i] > listOfTower[not_found[-1]]:
        for_answer[not_found.pop()] = i+1

    not_found.append(i)
    i-=1

for item in for_answer:
    print(item,end = " ")


