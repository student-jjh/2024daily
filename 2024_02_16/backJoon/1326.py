from collections import deque
move = [1,-1]
N = int(input())

lst = list(map(int,input().split()))
visited = [-1 for _ in range(N)]
start, end = map(int,input().split())
start -= 1
end -= 1

visited[start] = 0

queue = deque()
queue.append(start)

while queue:
    j = queue.popleft()

    for k in range(j+lst[j],N,lst[j]):

        dj = k

        if dj == end and visited[dj] == -1:
            visited[dj] = visited[j] +1

        if visited[dj] == -1:
            visited[dj] = visited[j] +1
            queue.append(dj)

    for k in range(j-lst[j],-1,-lst[j]):

        dj = k

        if dj == end and visited[dj] == -1:
            visited[dj] = visited[j] +1

        if visited[dj] == -1:
            visited[dj] = visited[j] +1
            queue.append(dj)

print(visited[end])