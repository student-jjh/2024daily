import sys
sys.setrecursionlimit(50000)
input = sys.stdin.readline


N,M = map(int,input().split())

parent= [i for i in range(N+1)]


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

cycle = 0
temp = []
for i in range(1,M+1):
    a,b = map(int,input().split())
    temp.append([a,b])

for i in range(1,M+1):
    a,b = temp[i-1]
    A = find_all(a)
    B = find_all(b)

    if A == B:
        print(i)
        cycle = i
        break
    else:
        union_all(a, b)

if cycle == 0:
    print(0)




