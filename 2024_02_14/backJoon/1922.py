# 파인드 유니온 만들고 답 제출 1트 고
# 힙큐로 최소먼저 뽑기 ㄱ
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
M = int(input())
q = []
parent = [i for i in range(N+1)]
for _ in range(M):
    a,b,c = map(int,input().split())
    heapq.heappush(q,(c,a,b))

cnt = 0
answer = 0
while q:
    c,a,b = heapq.heappop(q)
    if find_all(a) != find_all(b):
        union_all(a,b)
        answer += c
        cnt +=1

    if cnt == N-1:
        break
print(answer)





