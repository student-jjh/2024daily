N,M = map(int,input().split())

# 동전의 종류를 담을 List
coins = []

for_answer = [10001 for _ in range(10001)]

for _ in range(N):
    temp = int(input())
    coins.append(temp)
    for_answer[temp] = 1

coins.sort()

for i in range(coins[0] + 1,M+1):

    for coin in coins:
        if i - coin < 1:
            break

        elif for_answer[i-coin] == 0:
            continue
            
        for_answer[i] = min(for_answer[i],for_answer[i-coin] + 1)


if for_answer[M] == 10001:
    print(-1)
else:
    print(for_answer[M])






