n = int(input())
w = []
v = []
for _ in range(n):
  wi, vi = map(int, input().split())
  w.append(wi)
  v.append(vi)
W = int(input())

dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

for a in range(n):
  i = n - a - 1
  for j in range(W + 1):
    if j < w[i]:
      dp[i][j] = dp[i + 1][j]
    else:
      dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])
print(dp[0][W])