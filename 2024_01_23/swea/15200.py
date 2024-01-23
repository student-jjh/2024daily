
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int,input().split())

    Ai = list(map(int,input().split()))
    Bj = list(map(int,input().split()))
    answer= -10000000000
    if M >= N:
        M,N = N,M
        Ai,Bj = Bj,Ai

    for i in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += Ai[i+j] * Bj[j]

        answer = max(temp,answer)

    print(f"#{test_case} {answer}")