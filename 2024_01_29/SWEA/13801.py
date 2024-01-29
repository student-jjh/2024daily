
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(str,input().split())

    break_ok = False

    while break_ok == False:
        check = 0
        temp_str = ""
        while check < len(M)-1:
            if M[check] != M[check + 1]:
                temp_str = temp_str + M[check]
                check +=1
            else:
                check += 2
        if check == len(M)-1:
            temp_str += M[check]
        if M == temp_str:
           break_ok = True

        M = temp_str

    print(f"#{test_case} {temp_str}")