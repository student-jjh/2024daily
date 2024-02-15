N = int(input())

a,b,c = map(int,input().split())

for _ in range(N-1):
    A,B,C = map(int,input().split())

    A += min(b,c)
    B += min(a,c)
    C += min(a,b)

    a,b,c  = A,B,C

    print(a,b,c)