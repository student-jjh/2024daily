def recur(num):
    if num == N:
        if sum(answer) == M:
            print(*answer)
        return

    for i in range(1,7):
        answer.append(i)
        recur(num+1)
        answer.pop()




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    answer = []
    print(f"#{test_case}")
    recur(0)



