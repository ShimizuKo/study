N = int(input())
L = list(map(int, input().split()))

ans = 0
while N > 1:
  mii1 = 0
  mii2 = 1
  if L[mii1] > L[mii2]:
    mii1, mii2 = mii2, mii1
  
  for i in range(2, N):
    if L[i] < L[mii1]:
      mii2 = mii1
      mii1 = i
    elif L[i] < L[mii2]:
      mii2 = i
  
  t = L[mii1] + L[mii2]
  ans += t

  if mii1 == N - 1:
    mii1, mii2 = mii2, mii1
  L[mii1] = t
  L[mii2] = L[N - 1]
  N -= 1

print(ans)