N,M = map(int,input().split())
dict = {
    "D":(1,0),
    "R":(0,1),
    "U":(-1,0),
    "L":(0,-1),
}
graph = []
parent = [[[] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        parent[i][j] = [i,j]


for _ in range(N):
    graph.append(list(input()))

def find_all(X):
    if parent[X[0]][X[1]] != [X[0],X[1]]:
        parent[X[0]][X[1]] = find_all(parent[X[0]][X[1]])

    return parent[X[0]][X[1]]

def union_all(A,B):
    A = find_all(A)
    B = find_all(B)

    if A[0] > B[0]:
        parent[A[0]][A[1]] = B

    elif A[0] == B[0] and A[1] > B[1]:
        parent[A[0]][A[1]] = B

    else:
        parent[B[0]][B[1]] = A

for i in range(N):
    for j in range(M):
        di = i + dict[graph[i][j]][0]
        dj = j + dict[graph[i][j]][1]

        if find_all([i,j]) != find_all([di,dj]):
            union_all([i,j],[di,dj])

for i in range(N):
    for j in range(M):
        find_all([i,j])
answer = set()
for line in parent:
    for lst in line:
        answer.add(tuple(lst))

print(len(answer))

