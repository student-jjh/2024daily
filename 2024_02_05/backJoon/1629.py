A,B,C = map(int,input().split())
A = A % C
answer = 1
for _ in range(B):
    answer = (answer * A) % C

print(answer)