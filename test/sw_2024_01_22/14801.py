
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    temp = input()
    answer  = 0
    check = 0
    for i in range(N):
        if temp[i] == '1':
            check +=1
        else:
            check = 0
        answer = max(answer,check)
    print(f"#{test_case} {answer}")