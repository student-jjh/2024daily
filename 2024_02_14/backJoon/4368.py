#  처음에는 날먹하려고, 소트 두번 하고 답 구하려고 했는데 실패
#  정상적으로 풀어보자
import math
import heapq

def find_all(X):
    if parent[X] != X:
        parent[X] = find_all(parent[X])

    return parent[X]

def union_all(A,B):
    A = find_all(A)
    B = find_all(B)

    if A > B:
        parent[B] = A
    else:
        parent[A] = B

N = int(input())
graph = []
parent = [i for i in range(N+1)]
for _ in range(N):
    graph.append(list(map(float,input().split())))

def cal(A,B):
    return math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

q = []
for i in range(N-1):
    for j in range(i+1,N):
        heapq.heappush(q,(cal(graph[i],graph[j]),i,j))
cnt = 0
answer = 0

while q:
    caled,i,j = heapq.heappop(q)
    if find_all(i) != find_all(j):
        union_all(i,j)
        answer += caled
        cnt +=1

    if cnt == N-1:
        break

# 정답 출력 준비
print(f"{answer:.2f}")
