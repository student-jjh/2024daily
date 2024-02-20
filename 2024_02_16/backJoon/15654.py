N,M = map(int,input().split())

temp_lst = list(map(int,input().split()))
temp_lst.sort()
visited = [False for _ in range(N)]
lst = []
def recur(num):
    if num == M:
        print(*lst)
        return

    for i in range(N):
        if visited[i] == False:
            lst.append(temp_lst[i])
            visited[i] = True
            recur(num+1)
            lst.pop()
            visited[i] = False


recur(0)
