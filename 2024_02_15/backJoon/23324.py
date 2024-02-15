import sys
sys.setrecursionlimit(100000)

N,M,K = map(int,input().split())

parent = [i for i in range(N+1)]

def find_all(X):
    if parent[X] != X:
        parent[X] = find_all(parent[X])

    return parent[X]

def union_all(A,B):
    A = find_all(A)
    B=  find_all(B)

    if A > B:
        parent[B] = A

    else:
        parent[A] = B

for i in range(M):

    a,b = map(int,input().split())
    if i +1 == K :
        continue

    A= find_all(a)
    B =find_all(b)

    if A != B:
        union_all(A,B)

for i in range(len(parent)):
    find_all(i)
check = set(parent[1:])
if len(check) == 1:
    print(0)
else:
    print(parent.count(list(check)[0]) * parent.count(list(check)[1]))
