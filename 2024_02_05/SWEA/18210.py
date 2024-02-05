
def recut(num):
    global ans
    if num == N+1:
        print(f"#{test_case}",end = ' ')
        print(*ans)
        return

    ans.append(str(num))
    recut(num+1)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    ans = []
    N = int(input())

    recut(1)