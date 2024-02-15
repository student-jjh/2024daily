N = int(input())

graph = []

for _ in range(N):
    graph.append(list(map(int,input().split())))

answer =0

for i in range(1,N-1):
    answer += ((graph[i][0]-graph[0][0]) * (graph[i+1][1] - graph[0][1]) - (graph[i+1][0]-graph[0][0]) * (graph[i][1] - graph[0][1]) )

print(f"{abs(answer)/2:.1f}")