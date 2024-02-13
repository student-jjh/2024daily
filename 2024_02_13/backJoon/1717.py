import sys

N, M = map(int,sys.stdin.readline().rstrip().split(" "))

parent = [i for i in range(N+1)]

def find_all(x):
    if parent[x] != x:
        parent[x] = find_all(parent[x])

    return parent[x]

def union_all(A,B):
    A = find_all(A)
    B = find_all(B)

    if A > B:
        parent[B] = A
    else:
        parent[A] = B

for _ in range(M):
    seq,A,B = map(int,sys.stdin.readline().rstrip().split())

    if seq == 0:
        union_all(A,B)

    else:
        A = find_all(A)
        B = find_all(B)
        if A == B:
            print("YES")
        else:
            print("NO")