N = int(input())

food = list(map(int,input().split()))

for_log = [0 for _ in range(N)]

for_log[0],for_log[1] = food[0],food[1]

for i in range(2,N):
    for_log[i] = max(for_log[i-1],for_log[i-2]+food[i])

print(for_log[-1])