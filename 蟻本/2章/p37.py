N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

INF = float("inf")
d = [[INF for _ in range(M)] for _ in range(N)]
sx, sy = 0, 0
gx, gy = 0, 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
  queue = [[sx, sy]]
  d[sx][sy] = 0
  
  while len(queue):
    p = queue.pop(0)
    if p[0] == gx and p[1] == gy:
      break
    
    for i in range(4):
      nx = p[0] + dx[i]
      ny = p[1] + dy[i]

      if 0 <= nx and nx < N and 0 <= ny and ny < M and maze[nx][ny] != "#" and d[nx][ny] == INF:
        queue.append([nx, ny])
        d[nx][ny] = d[p[0]][p[1]] + 1
  return d[gx][gy]

for i in range(N):
  for j in range(M):
    if maze[i][j] == "S":
      sx, sy = i, j
    if maze[i][j] == "G":
      gx, gy = i, j
res = bfs()
print(res)