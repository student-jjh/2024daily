srt = input()

N = len(srt)
for_check = ["(",")"]
for_answer = ""
stack = []
i = 0
while i < N-1:
    if srt[i] == "(":
        stack.append(srt[i])
        i+=1
        temp = ""

    elif srt[i] not in for_check and srt[i+1] not in for_check:
        for_answer += srt[i]

