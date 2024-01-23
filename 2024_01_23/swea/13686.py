

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    temp = list(map(int,input().split()))

    temp = temp[::-1]
    mx = temp[0]
    answer = 0
    for i in range(N):
        if temp[i] > mx :
            mx = temp[i]

        else:
            answer += mx-temp[i]

    print(f"#{test_case} {answer}")