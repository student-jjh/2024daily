V,E = map(int,input().split())

parent = [i for i in range(V+1)]

def find_all(X):
    if parent[X] != X:
        parent[X] = find_all(parent[X])

    return parent[X]

def union_all(A,B):
    A = find_all(A)
    B = find_all(B)

    if A > B:
        parent[A] = B

    else:
        parent[B] = A

graph = []
for _ in range(E):
    a,b,c = map(int,input().split())
    graph.append((c,a,b))

answer = 0
cnt = 0
graph.sort()

for c,a,b in graph:
    if find_all(a) != find_all(b):
        union_all(a,b)
        answer +=c
        cnt +=1

    if cnt ==V-1:
        break

print(answer)