import math

N = int(input())

temp = []

for _ in range(N):
    temp.append((float(input())))
answer =0
for i in range(N):
    now = temp[i]
    if now > answer:
        answer = now
    for j in range(i+1,N):
        now *= temp[j]
        if now > answer:
            answer = now


print('%0.3f' % answer)