maxs = 0
x = 0
y = 0

for i in range(9):
    temp_number = list(map(int,input().split()))

    temp_max = max(temp_number)

    if temp_max > maxs:
        x = i
        y = temp_number.index(temp_max)
        maxs = temp_max
print(maxs)
print(x+1,y+1)

