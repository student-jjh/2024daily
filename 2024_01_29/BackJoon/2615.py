board = [list(map(int, input().split())) for _ in range(19)]

visited = 0

# 사방 탐색용 (우, 하, 우하, 좌하)
dr, dc = (0, 1, 1, 1), (1, 0, 1, -1)

# 한 칸씩 탐색
for i in range(19):
    for j in range(19):
        # 바둑알의 시작점인 경우
        c = board[i][j]
        if c:
            # 사방 탐색
            for d in range(4):
                # 이미 방문한 곳은 패스
                if not visited & 1 << (19 * 4 * i + 4 * j + d):
                    visited |= 1 << (19 * 4 * i + 4 * j + d)

                    # 연속된 바둑알 개수
                    cnt = 1

                    # 사방 탐색 시 다음 위치
                    ni = i + dr[d]
                    nj = j + dc[d]

                    # 범위 내에 있으면서 같은 바둑알이 있으면 개수 증가
                    while 0 <= ni < 19 and 0 <= nj < 19 and not visited & 1 << (19 * 4 * ni + 4 * nj + d) and board[ni][nj] == c:
                        visited |= 1 << (19 * 4 * ni + 4 * nj + d)
                        cnt += 1
                        ni += dr[d]
                        nj += dc[d]

                    # 연속된 바둑알이 5개인 경우, 승리
                    if cnt == 5:
                        print(c)
                        if d < 3:
                            print(i + 1, j + 1)
                        # 좌하 -> 우상인 경우, 맨 왼쪽에 있는 바둑알 출력
                        else:
                            print(ni - dr[d] + 1, nj - dc[d] + 1)
                        exit()

# 아직 승부가 결정되지 않은 경우
else:
    print(0)