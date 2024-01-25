N, M = map(int,input().split())

poke = {}

for i in range(1,N+1):
    name = input()
    poke[str(i)] = name
    poke[name] = i

for i in range(M):
    q = input()

    print(poke[q])