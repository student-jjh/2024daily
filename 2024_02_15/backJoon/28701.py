N = int(input())
answer = 0
answer_t = 0
for i in range(1,N+1):
    answer += i
    answer_t += i**3

print(answer)
print(answer**2)
print(answer_t)