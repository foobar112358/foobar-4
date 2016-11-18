#!/usr/bin/env python
from collections import deque

def bfs(maze):
    q = deque([(0,0,1)])
    vis = [[False for _ in xrange(len(maze[0]))] for _ in xrange(len(maze))]
    vis[0][0] = True

    while q:
        x, y, k = q.popleft()
        vis[x][y] = True
        if x == len(maze) - 1  and y == len(maze[0]) - 1:
            return k
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if abs(i * j) == 1:
                    continue
                nx, ny = x + i, y + j
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
                    if not vis[nx][ny] and maze[nx][ny] == 0:
                        q.append((nx, ny, k+1))
    return 2 << 32

def answer(maze):
    ans = bfs(maze)

    # for i in xrange(len(maze)):
    #     for j in xrange(len(maze[0])):
    #         if maze[i][j] == 1:
    #             maze[i][j] = 0
    #             ans = min(bfs(maze), ans)
    #             maze[i][j] = 1
    return ans


print answer([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 1, 0], [1, 1, 1, 0]])
