N,M = map(int,input().split())

temp = []

for i in range(2):
    temp_list = []
    for j in range(N):
        for_add = list(map(int,input().split()))
        temp_list.append((for_add))

    temp.append((temp_list))

answer = []
for i in range(N):
    result = [j+i for i,j in zip(temp[0][i],temp[1][i])]
    answer.append(result)

for item in answer:
    for number in item:
        print(number, end = " ")
    print()


