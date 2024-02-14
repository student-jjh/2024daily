import heapq
N,M = map(int,input().split())
parent = [i for i in range(N+1)]
q = []

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

for _ in range(M):
    a,b,c = map(int,input().split())

    heapq.heappush(q,(c,a,b))

answer = 0
cnt = 0
mn = 0
while q:
    c,a,b = heapq.heappop(q)

    if find_all(a) != find_all(b):
        union_all(a,b)
        answer +=c
        if c > mn:
            mn = c
        cnt +=1

    if cnt == N-1 :
        break

print(answer - mn)