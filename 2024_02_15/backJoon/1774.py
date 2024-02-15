N,M = map(int,input().split())
parent = [i for i in range(N+1)]
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

lst_point = []
for _ in range(N):
    lst_point.append(list(map(int,input().split())))

cnt = 0

for _ in range(M):
    a,b = map(int,input().split())
    if find_all(a) != find_all(b):
        cnt += 1
        union_all(a, b)

lst = []

for i in range(N-1):
    for j in range(i+1,N):
        lst.append([((lst_point[i][0] - lst_point[j][0])**2 + (lst_point[i][1] - lst_point[j][1])**2)**0.5,i+1,j+1])

lst.sort(reverse=True)



answer = 0

while lst and cnt != N-1:
    dist,i,j = lst.pop()

    if find_all(i) != find_all(j):
        answer += dist
        cnt +=1
        union_all(i,j)

print(f"{answer:.2f}")
