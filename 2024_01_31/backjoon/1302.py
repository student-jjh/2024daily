N = int(input())
dict = {}
for _ in range(N):
    name = input()
    if name in dict:
        dict[name] +=1
    else:
        dict[name] = 1

temp = list(dict.items())
temp.sort(reverse=True)
temp.sort(key = lambda x: x[1])
print(temp[-1][0])