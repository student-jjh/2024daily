from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


# 벽을 밤이어도 무조건 2스텝 이동하게 되면, 최단거리가 아님에도 벽을 2스텝으로 부수고 가는 경로가 잡힌다.

def bfs(c, x, y):
    q = deque()
    steps[c][x][y] = 1
    q.append((c, x, y))
    while q:
        c, x, y = q.popleft()
        c_step = steps[c][x][y]
        if (x, y) == goal:
            return steps[c][x][y]
        stay = False
        for d in range(len(dx)):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < h and 0 <= ny < w and not steps[c][nx][ny]:
                if board[nx][ny] == '0':  # 길이면 그냥 처리
                    steps[c][nx][ny] = c_step + 1
                    q.append((c, nx, ny))
                elif board[nx][ny] == '1' and c < crush:
                    if c_step % 2 != 0:  # 현재 스텝이 홀수면 낮, 짝수면 밤.
                        # 1. 낮인가? -> 스텝 1단
                        steps[c + 1][nx][ny] = c_step + 1
                        q.append((c + 1, nx, ny))
                    else:
                        stay = True
                        # 2. 벽이고 밤이면 스테이.
                        q.append((c, x, y))
        if stay:
            steps[c][x][y] += 1
    return -1


# TC = int(input())
#
# for tc in range(1, TC + 1):
h, w, crush = map(int, input().split())
steps = [[[0 for _ in range(w)] for _ in range(h)] for _ in range(crush + 1)]
board = [list(input()) for _ in range(h)]
goal = (h - 1, w - 1)

answer = bfs(0, 0, 0)
print(answer)