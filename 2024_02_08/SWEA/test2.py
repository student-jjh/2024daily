
def recur(time,point,size):
    global  answer
    if time == M or point == N:
        if size > answer:
            answer = size
        return

    if point + 2 < N:
        recur(time+1,point + 2,size // 2 + line[point + 2])

    recur(time + 1, point +1, size + line[point + 1])
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # N = 직선구간의 길이 M = 굴리는 제한시간
    N,M = map(int,input().split())
    N = N -1

    line = list(map(int,input().split()))

    answer = -1

    recur(0,-1,1)

    print(f"#{test_case} {answer}")