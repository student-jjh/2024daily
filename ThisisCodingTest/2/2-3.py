temp = input()

check_box = ['a','b','c','d','e','f','g','h']

x = check_box.index(temp[0])
y = int(temp[1])-1

test_case = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

answer = 0

for move in test_case:
    temp_x = x + move[0]
    temp_y = y + move[1]

    if temp_x < 0 or temp_x >8 or temp_y<0 or temp_y>8:
        continue

    answer += 1

print(answer)