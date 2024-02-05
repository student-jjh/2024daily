def fibo(N):
    if N == 1 or N == 2:
        return 1

    return fibo(N-1) + fibo(N-2)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    print(f"#{test_case} {fibo(N)}")