n = int(input())
w = []
v = []
for _ in range(n):
  wi, vi = map(int, input().split())
  w.append(wi)
  v.append(vi)
W = int(input())

dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

for i in range(n):
  for j in range(W + 1):
    if j < w[i]:
      dp[i + 1][j] = dp[i][j]
    else:
      dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - w[i]] + v[i])
print(dp[n][W])