N = int(input())
temp = []
for _ in range(N):
    temp.append(int(input()))
diff = []
for i in range(1,N):
    diff.append(temp[i]-temp[i-1])
def gcd(a,b):
    while b > 0:
        a,b = b, a%b
    return a
temps = diff[0]
for i in range(1,N-1):
    temps = gcd(temps,diff[i])
answer = 0
for di in diff:
    answer += di // temps-1
print(answer)

