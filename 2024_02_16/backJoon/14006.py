T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    trucks = []
    for _ in range(N):
        trucks.append(list(map(int,input().split())))

    trucks.sort(key = lambda x : x[1])

    answer = []
    answer.append(trucks[0])

    for i in range(1,N):
        if trucks[i][0] >= answer[-1][1]:
            answer.append(trucks[i])

    print(f"#{test_case} {len(answer)}")


