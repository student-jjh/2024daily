T = int(input())

for _ in range(T):
    N = str(bin(int(input())))
    N = N[2:]
    for i in range(-1,-len(N)-1,-1):
        if N[i] == '1':
            print(-i-1,end = " ")

    print()
