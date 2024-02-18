vowels = ['a','i','u','e','o']

N = int(input())
temp = input()
cnt = 0 
for i in range(N):
    if temp[i] in vowels:
        cnt +=1

print(cnt)
