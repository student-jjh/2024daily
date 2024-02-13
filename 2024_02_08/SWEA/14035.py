move = [(1,0),(-1,0),(0,1),(0,-1)]

def recur(num,i,j):
    global answer
    if num == m:
        if tuple(answer_lst) not in answer_set:
            answer_set.add(tuple(answer_lst))
            answer +=1
        return

    for k in range(4):
        di = i + move[k][0]
        dj = j + move[k][1]

        if di<0 or di >=4 or dj < 0 or dj >= 4:
            continue

        answer_lst.append(graph[di][dj])
        recur(num + 1,di,dj)
        answer_lst.pop()


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    graph = []
    visited = [[False for _ in range(4)] for _ in range(4)]
    for _ in range(4):
        graph.append(list(map(int,input().split())))
    answer_lst = []
    answer = 0
    answer_set = set()
    m = 7

    for i in range(4):
        for j in range(4):
            answer_lst.append(graph[i][j])
            recur(1,i,j)
            answer_lst.pop()

    print(f"#{test_case} {answer}")