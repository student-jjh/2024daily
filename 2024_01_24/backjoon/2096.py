N = int(input())

A,B,C = 0,0,0
a,b,c = 0,0,0

for i in range(N):
    _a,_b,_c = map(int,input().split())

    A,B,C = _a + max(A,B), _b+ max(A,B,C), _c + max(B,C)
    a,b,c = _a + min(a,b), _b+ min(a,b,c), _c + min(b,c)


print(max(A,B,C),min(a,b,c))
