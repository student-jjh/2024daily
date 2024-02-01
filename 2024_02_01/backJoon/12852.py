from collections import deque

N = int(input())
visited = set()

def bfs(N):
    queue = deque()
    queue.append((N, [N]))
    while queue:
        N,visited_list = queue.popleft()
        if N%3 == 0 and N//3 not in visited:
            if N // 3 == 1:
                return visited_list
            visited.add(N//3)
            temp = []
            temp.extend(visited_list)
            temp.append(N//3)
            queue.append([N//3,temp])

        if N%2 == 0 and N//2 not in visited:
            if N // 2 == 1:
                return visited_list
            visited.add(N//2)
            temp = []
            temp.extend(visited_list)
            temp.append(N//2)
            queue.append([N//2,temp])

        if N -1 not in visited:
            if N -1 == 1:
                return visited_list
            visited.add(N-1)
            temp = []
            temp.extend(visited_list)
            temp.append(N - 1)
            queue.append([N - 1, temp])

temp = bfs(N)
temp.append(1)
print(len(temp)-1)
print(*temp)
