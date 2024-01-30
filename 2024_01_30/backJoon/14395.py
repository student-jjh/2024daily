from collections import deque

s, t = map(int,input().split())
visited = {}

def bfs(s,t,srt):

    if s == t:
        return 0
    visited[str(s)] = 1
    queue = deque()
    queue.append((s,t,srt))

    while queue:
        s,t,srt = queue.popleft()

        ms =  s * s
        if str(ms) not in visited:
            if ms == t:
                return srt+"*"
            elif ms < t:
                queue.append((ms,t,srt+"*"))
                visited[str(ms)] = 1

        mp = s + s
        if str(mp) not in visited:

            if mp == t:
                return srt + "+"
            elif mp < t:
                queue.append((mp,t,srt+"+"))
                visited[str(mp)] = 1

        mm = s -s
        if str(mm) not in visited:
            if mm == t:
                return srt + "-"
            else:
                queue.append((mm,t,srt+"-"))

        if s !=0:
            ms = 1
            if str(ms) not in visited:
                if ms == t:
                    return srt + "/"
                else:
                    queue.append((ms,t,srt+"/"))
    return -1


print(bfs(s,t,""))