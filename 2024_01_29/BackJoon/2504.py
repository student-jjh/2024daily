question = input()

stack = []

for_answer = ""

for word in question:

    if word == "(":
        stack.append("(")
        if for_answer == "":
            for_answer += "2*("
        else:
            for_answer += "+2*("
    elif word == "[":
        stack.append("[")
        if for_answer =="":
            for_answer += "3*("
        else:
            for_answer += "+3*("

    elif word ==  ")":
        if stack == []:
            for_answer = 0
            break
        temp = stack.pop()

        if temp == "(":
            if for_answer[-1] == "+":
                for_answer +="0)"
            elif for_answer[-1] == ")":
                for_answer += "*1)"
            else:
                for_answer += "1)+"
        else:

            for_answer = 0
            break
    elif word =="]":
        if stack == []:
            for_answer = 0
            break
        temp = stack.pop()
        if temp == "[":
            if for_answer[-1] == "+":
                for_answer +="0)"
            elif for_answer[-1] ==")":
                for_answer +="*1)"
            else:
                for_answer += "1)+"
        else:
            for_answer =0
            break
if stack != []:
    for_answer = 0
if for_answer == 0:
    print(0)
else:
    if for_answer[-1] == "+":
        for_answer +="0"
    result = eval(for_answer)
    print(result)
