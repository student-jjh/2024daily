game = {"Y":1,"F":2,"O":3}

N,G = map(str,input().split())
player = set()
for _ in range(int(N)):
    temp = input()
    player.add(temp)

K = len(player)

print(K//game[G])