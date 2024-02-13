N = int(input())
M = int(input())
parent = [i for i in range(N+1)]

def find_all(X):
    if parent[X] != X:
        parent[X] = find_all(parent[X])

    return parent[X]

def union_all(A,B):
    A = find_all(A)
    B = find_all(B)

    if A == B:
        return
    elif A > B:
        parent[B] = A

    else:
        parent[A] = B

for i in range(1,N+1,1):
    temp = list(map(int,input().split()))
    for j in range(N):
        if temp[j] == 1:
            union_all(i,j+1)
routh = list(map(int,input().split()))
temp = set()
for i in routh:
    temp.add(find_all(i))

if len(temp) == 1:
    print("YES")
else:
    print("NO")


