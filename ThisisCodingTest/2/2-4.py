S = input()

temp_list = []
add_num = 0

number_list = ['0','1','2','3','4','5','6','7','8','9']

for words in S:
    if words in number_list:
        add_num += int(words)

    else:
        temp_list.append(words)

temp_list.sort()

temp_str = ''.join(temp_list)
print(temp_str + str(add_num))