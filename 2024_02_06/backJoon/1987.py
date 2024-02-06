# from collections import deque
# DFS로 풀어야 할 듯?
import sys

input = sys.stdin.readline
move = [(1,0),(-1,0),(0,1),(0,-1)]

# 그래프의 세로 가로 입력
N,M = map(int,input().split())
# 알파벳 숫자만큼 생성 (ord로 계산해서 방문 확인 예정)
visited = [0 for _ in range(26)]

graph = []
for _ in range(N):
    graph.append(list(input()))
ans = 0
def dfs(graph,v,visited,cnt):
    global ans
    if cnt > ans:
        ans = cnt
    i,j = v

    visited[ord(graph[i][j])-65] = True
    for k in range(4):
        di = i + move[k][0]
        dj = j + move[k][1]

        if di < 0 or di >=N or dj < 0 or dj>=M:
            continue

        if visited[ord(graph[di][dj])-65] == False:
            visited[ord(graph[di][dj]) - 65] = True
            dfs(graph,(di,dj),visited,cnt+1)
            visited[ord(graph[di][dj]) - 65] = False

dfs(graph,(0,0),visited,1)

print(ans)

# print(ord("A")) = 65
# print(ord("Z")) = 90