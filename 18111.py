N,M,B = map(int,input().split())

temp_list = []

for i in range(N):
    temp = list(map(int,input().split()))
    temp_list += temp

# print(temp_list)

temp_list.sort(reverse=True)
for_answer = 1000000000000000000
height = 0

for number in range(temp_list[-1],temp_list[0]+1):

    temp_B = B
    for block in temp_list:

        answer = 0
        if block > number:
            temp_B += (block-number)
            answer += 2*(block-number)
        else:
            if temp_B-(number-block) < 0:
                break

            else:
                temp_B -= (number - block)
                answer += (number - block)

    if for_answer > answer and height <= number:
        height = number
        for_answer = answer
    print(temp_list)
    print(for_answer,answer,number)

print(f"{answer} {height}")