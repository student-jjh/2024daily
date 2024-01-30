T = int(input())

for _ in range(T):

    N,M = map(int,input().split())

    answer = 1

    for i in range(N):
        answer *= (M-i)
        answer /= i+1

    print(int(answer))