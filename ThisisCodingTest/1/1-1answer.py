n ,k = map(int,input().split())

result = 0 

while True:
    temp = (n // k) * k

    result += (n - temp)

    n = temp

    if n < k:
        break

    result += 1

    n //= k

result += (n-1)

print(result)

