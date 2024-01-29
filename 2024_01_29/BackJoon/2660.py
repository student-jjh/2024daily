from collections import deque

N = int(input())
graph = [[] for _ in range(N+1)]
for_answer = [0 for _ in range(N+1)]

while True:
    a,b = map(int,input().split())

    if a == -1 and b == -1:
        break

    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    visited = [-1 for _ in range(N+1)]
    visited[i] = 0

    queue = deque()
    queue.append(i)

    while queue:
        now = queue.popleft()

        for item in graph[now]:
            if visited[item] == -1:

                visited[item] = visited[now] +1
                queue.append(item)
    for_answer[i] = max(visited)

temp = for_answer[1:]
mm = min(temp)
answer = []
for i in range(len(temp)):
    if temp[i] == mm:
        answer.append(i+1)

print(f"{mm} {temp.count(mm)}")
print(*answer)
