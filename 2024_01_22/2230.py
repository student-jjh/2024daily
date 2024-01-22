N, M = map(int,(input().split()))

temp = []
for i in range(N):
    temp.append(int(input()))


temp.sort()
temp.append(0)

start = 0
end = 1
sm = temp[end] - temp[start]
answer = 100000000000
while end != N and start!=N:

    if sm >= M:
        if sm < answer:
            answer = sm
        sm += temp[start]
        start += 1
        if start <N:

            sm -= temp[start]

    else:
        sm -= temp[end]
        end += 1
        if end < N:
            sm += temp[end]

print(answer)