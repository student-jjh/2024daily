N = int(input())
temp = []
cal = round(N * 0.15)
if N ==0:
    print(0)
else:

    for i in range(N):
        temp_input = int(input())
        temp.append(temp_input)

    temp.sort()

    for_answer = temp[cal:N - cal]

    print(round(sum(for_answer) / len(for_answer)))