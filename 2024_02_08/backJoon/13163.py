N = int(input())

for _ in range(N):
    temp = list(map(str,input().split()))
    temp[0] = "god"
    print("".join(temp))
