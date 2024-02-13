

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    N,L = map(int,input().split())

    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))

    score = 0

    scr = 0
    visited = [False for _ in range(N)]
    def recur(num,answer,scr):
        global score
        if sum(answer) > L:
            return

        if num == N:
            if sum(answer) <=L:
                score = max(score,scr)
            return


        recur(num+1,answer,scr)
        recur(num+1,answer+[graph[num][1]],scr+graph[num][0])

    recur(0,[],0)

    print(f"#{test_case} {score}")
