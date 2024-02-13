N = int(input())
move = [(1,0),(-1,0),(0,1),(0,-1)]

graph = []
answer = [0 for _ in range(5)]

for _ in range(N):
    graph.append(list(input()))

for line in graph:
    print(line)
heart = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == "*":
            cnt = 0
            for k in range(4):
                di = i + move[k][0]
                dj = j + move[k][1]

                if di < 0 or di >=N or dj < 0 or dj >=N:
                    break

                if graph[di][dj] == "*":
                    cnt +=1
            if cnt == 4:
                heart = (i,j)
                break

        if heart:
            break
