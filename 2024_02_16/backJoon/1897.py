d, word = map(str,input().split())
words = set()
mx = 0
for _ in range(int(d)):
    temp = input()
    if len(temp) > mx:
        mx = len(temp)

    words.add(temp)

def recur(num):
    if len(word) + num == mx:
        pass