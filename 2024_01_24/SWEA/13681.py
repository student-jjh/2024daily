
T = int(input())

def is_sdk(graph):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 가로 확인
    for i in range(9):
        temp = graph[i][:]
        temp.sort()
        if temp != check:
            return 0

    # 세로 확인
    temp_graph = list(zip( *graph ))
    for i in range(9):
        temp = list(temp_graph[i][:])
        temp.sort()
        if temp != check:
            return 0

    # 3 X 3 확인
    for i in range(3,10,3):
        for j in range(3,10,3):
            temp = []
            for k in range(i-3,i):
                for v in range(j-3,j):
                    temp.append(graph[k][v])
            temp.sort()
            if temp != check:
                return 0
    return 1
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    graph = []

    for _ in range(9):
        graph.append(list(map(int,input().split())))


    print(f"#{test_case} {is_sdk(graph)}")