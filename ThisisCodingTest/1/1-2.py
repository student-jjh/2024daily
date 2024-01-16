N = input()

number_list = list(map(int,N.split("")))

answer = 0 

for number in number_list:
    if answer > 1  and number >1 :
        answer *= number
    else:
        answer += number
print(answer)   