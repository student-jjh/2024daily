N = int(input())

hp = list(map(int,input().split()))
joy = list(map(int,input().split()))

dp = [[0 for _ in range(100)] for _ in range(N)]
