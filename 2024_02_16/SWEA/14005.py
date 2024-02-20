T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    containers = list(map(int,input().split()))
    trucks = list(map(int,input().split()))
    # 무거운거 부터, 무거운걸 실을 수 있는 것 부터 빼는 중
    containers.sort()
    trucks.sort()
    answer = 0
    while trucks and containers:
        truck = trucks.pop()


        while containers:
            container = containers.pop()
            if truck >= container:
                answer += container
                break
    print(f"#{test_case} {answer}")