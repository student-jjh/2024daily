N = int(input())

temp = list(map(int,input().split()))

temp = list(set(temp))
temp.sort()
print(*temp)
