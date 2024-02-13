N = int(input())
pattern = (input().split("*"))

for _ in range(N):
    temp = input()
    if len(temp) < len(pattern[0]) + len(pattern[1]):
        print("NE")
        continue
    # print(temp[:len(pattern[0])],pattern[0],temp[-len(pattern[1]):],pattern[1])
    if temp[:len(pattern[0])] == pattern[0] and temp[-len(pattern[1]):] == pattern[1]:
        print("DA")
    else:
        print("NE")