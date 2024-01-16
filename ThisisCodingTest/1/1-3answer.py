N = int(input())

scare_list = list(map(int,input().split()))

scare_list.sort()

result = 0 
count = 0

for i in scare_list:
    count += 1

    if count >= i:
        result +=1 
        count = 0

print(result)