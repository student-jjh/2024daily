from itertools import permutations
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
temp = list(permutations(a))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    graph = []

    for _ in range(N):
        graph.append(list(map(int,input().split())))

