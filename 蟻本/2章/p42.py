C = list(map(int, input().split()))
A = int(input())

V = [1, 5, 10, 50, 100, 500]
ans = 0

for i in range(6):
  t = min(A // V[5 - i], C[5 - i])
  A -= t * V[5 - i]
  ans += t

print(ans)