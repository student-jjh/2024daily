N = int(input())
def good_word(words):
    stack = []
    for word in words:
        if stack == [] or stack[-1] != word:
            stack.append(word)
        else:
            stack.pop()
    if stack != []:
        return False
    return True


cnt = 0
for _ in range(N):
    lst = list(input())
    if good_word(lst) == True:
        cnt +=1

print(cnt)