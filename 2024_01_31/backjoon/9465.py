T = int(input())

for _ in range(T):
    n = int(input())

    sticker = []
    for _ in range(2):
        sticker.append(list(map(int,input().split())))



    for i in range(2,n):
        sticker[0][i] = max(sticker[0][i-1],sticker[0][i] + sticker[1][i-1])
        sticker[1][i] = max(sticker[1][i-1],sticker[1][i] + sticker[0][i-1])
    print(sticker)
    print(max(sticker[0][n-1],sticker[1][n-1]))






