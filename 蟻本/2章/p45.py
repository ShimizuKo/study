N = int(input())
S = input()

a = 0
b = N - 1
ans = ""
while a <= b:
  left = False
  for i in range(b - a + 1):
    if S[a + i] < S[b - i]:
      left = True
      break
    elif S[a + i] > S[b - i]:
      left = False
      break
  
  if left:
    ans += S[a]
    a += 1
  else:
    ans += S[b]
    b -= 1

print(ans)