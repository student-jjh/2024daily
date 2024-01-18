st = input()

def is_pal(st):
    length = len(st)

    for i in range(length):
        if st[i] != st[-(i+1)]:
            return 0

    return 1

print(is_pal(st))