def recur(sr):
    if len(sr) == 1:
        return int(sr)

    return recur(sr[:-1]) + int(sr[-1])


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = input()
    print(f"#{test_case} {recur(N)}")
