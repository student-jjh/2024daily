from collections import deque

N = int(input())
M = int(input())

prices = [[100001 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1,N+1):
    prices[i][i] = 0


for i in range(M):
    start, end, price = map(int, input().split())
    if  prices[start][end] > price:
        prices[start][end] = price

st, ed = map(int, input().split())

for_answer = prices[st]
def bfs(start, end):
    queue = deque()

    queue.append(start)

    while queue:

        now = queue.popleft()


        for i in range(1,N+1):
            if i == now or prices[now][i] == 100001:
                continue
            if for_answer[now] + prices[now][i] <= for_answer[i]:
                for_answer[i] = for_answer[now] + prices[now][i]
                queue.append(i)

    return for_answer[end]







print(bfs(st, ed))