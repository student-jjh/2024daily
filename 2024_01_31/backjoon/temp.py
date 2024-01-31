def split_paper(start_row, start_col, end_row, end_col, length):
    global paper
    global N
    global blue_paper
    global white_paper

    if length != 1:
        next_length = length // 2
        next_visit = []
        for i in range(2):
            for j in range(2):
                next_visit.append(
                    [start_row + next_length * i, start_col + next_length * j, start_row + next_length * (i + 1),
                     start_col + next_length * (j + 1), next_length])

    blue_count = 0
    white_count = 0

    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if blue_count > 0 and white_count > 0:
                for element in next_visit:
                    split_paper(element[0], element[1], element[2], element[3], element[4])
                return

            color = paper[i][j]
            if color == 1:
                blue_count += 1
                continue
            white_count += 1
    if blue_count == length * length:
        blue_paper += 1
        return
    if white_count == length * length:
        white_paper += 1
        return


N = int(input())
paper = []
for i in range(N):
    paper.append(list(map(int, input().split())))

blue_paper = 0
white_paper = 0
split_paper(0, 0, N, N, N)
print(white_paper)
print(blue_paper)