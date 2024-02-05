def recur(num,si):
    if num == N:
        print(*answer)
        return

    for i in range(si,7):
        answer.append(i)
        recur(num+1,i)
        answer.pop()

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    answer = []
    N = int(input())
    print(f"#{test_case}")
    recur(0,1)
