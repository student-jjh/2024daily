temp = []
for i in range(1,9):
    temp.append((int(input()),i))

temp.sort()
temp = temp[-5:]
temp.sort(key = lambda x : x[1])

answer = 0
for i in range(5):
    answer += temp[i][0]

print(answer)
for i in range(5):
    print(temp[i][1],end = " ")