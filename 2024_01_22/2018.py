N = int(input())

start = sm = end = count = 1

while end != N:
    if sm == N:
        count +=1
        end +=1
        sm +=end
    elif sm > N:
        sm -= start
        start +=1
    else:
        end +=1
        sm +=end

print(count)