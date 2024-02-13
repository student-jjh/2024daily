def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union_all(A,B):
    _A = find(A)
    _B = find(B)

    if _A> _B:
        parent[_B] = _A
    else:
        parent[_A] = _B

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N,M = map(int,input().split())

    parent = [i for i in range(N+1)]
    apply = list(map(int,input().split()))
    for i in range(0,(M)*2,2):
        union_all(apply[i],apply[i+1])
    for i in range(1,N+1):
        find(i)
    print(f"#{test_case} {len(set(parent[1:]))}")