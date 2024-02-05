def recur(si,num):
    global cnt
    if num == M:
        if sum(answer) ==K:
            cnt +=1
        return

    for i in range(si,N):
        if visited[i] == False:
            answer.append(graph[i])
            visited[i] = True
            recur(i,num+1)
            answer.pop()
            visited[i] = False
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M,K = map(int,input().split())
    visited = [False for _ in range(N)]
    graph = list(map(int,input().split()))
    cnt = 0
    answer =[]
    recur(0,0)
    print(f"#{test_case} {cnt}")


