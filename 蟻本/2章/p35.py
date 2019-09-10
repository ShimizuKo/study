N, M = map(int, input().split())
field = [list(input()) for _ in range(N)]

def dfs(x, y):
  field[x][y] = "."

  for dx in range(-1, 2):
    for dy in range(-1, 2):
      nx = x + dx
      ny = y + dy
      if nx >= 0 and nx < N and ny >= 0 and ny < M and field[nx][ny] == "W":
        dfs(nx, ny)
  return

res = 0
for i in range(N):
  for j in range(M):
    if field[i][j] == "W":
      dfs(i, j)
      res += 1
print(res)