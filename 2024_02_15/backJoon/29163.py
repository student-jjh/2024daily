N = int(input())

lst = list(map(int,input().split()))

count = 0

for i in lst:
    if i % 2 == 0:
        count +=1

if count > N - count:
    print("Happy")

else:
    print("Sad")