N = int(input())

line = map(int, input().split())

if N == 1:
    print("B")

elif N == 2:
    if line[1] -line[0] == 0:
        a=1
        b=0
    elif line[0] == 0:
        b = line[1]
    elif line[1] == 0:
        pass



else:
    temp = (line[1] - line[0])
    if temp == 0:
        b = line[2] - line[1]

    else:
        a = (line[2] - line[1]) // temp
        b = line[1] - (line[0] * a)
