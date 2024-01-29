start = ["(","{"]
end = [")","}"]

def cross():
    temp = input()
    stack = []
    for i in temp:
        if i in start:
            stack.append(i)

        elif i in end:
            if stack ==[]:
                return 0
            for_check = stack.pop()
            if i == ")":
                if for_check == "(":
                    continue

                else:
                    return 0

            elif i == "}":
                if for_check == "{":
                    continue

                else:
                    return 0

    if stack == []:
        return 1

    else:
        return 0


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f"#{test_case} {cross()}")
