
def is_pas(sr):
    for i in range(len(sr)//2):
        if sr[i] != sr[-1-i]:
            return False
    return True

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    graph = []

    for _ in range(8):
        graph.append(list(input()))

    temp_graph = list(zip(* graph))

    # 가로 확인
    cnt = 0
    for i in range(8):
        for j in range(8-N+1):
            if is_pas(graph[i][j:j+N]):
                cnt +=1

    # 세로 확인
    for i in range(8):
        for j in range(8-N+1):
            if is_pas(temp_graph[i][j:j+N]):
                cnt +=1


    print(f"#{test_case} {cnt}")
