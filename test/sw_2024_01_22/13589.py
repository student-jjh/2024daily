T = int(input())
print(T)
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    temp = input()

    dic = {}
    for number in temp:

        if number in dic :
            dic[number] +=1

        else:
            dic[number] = 1

    for_answer = list(dic.items())
    for_answer.sort()
    for_answer.sort(key =lambda x: x[1])

    print(f"#{test_case} {for_answer[-1][0]} {for_answer[-1][1]}")