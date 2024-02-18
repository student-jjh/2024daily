for_check = ['a', 'e', 'i', 'o', 'u',"A",'E','O',"U"]

while True:
    temp = 0
    temp_input = input()

    if temp_input == "#":
        break

    for i in temp_input:
        if i in for_check:
            temp +=1

    print(temp)