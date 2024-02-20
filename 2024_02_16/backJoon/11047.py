N,K = map(int,input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

coins.sort()
answer = 0
while K > 0 and coins:
    coin = coins.pop()
    answer += K//coin
    K = K % coin

print(answer)
