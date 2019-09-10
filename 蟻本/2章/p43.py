n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

w = []
for i in range(n):
  w.append([s[i], t[i]])

w.sort(key = lambda x:x[1])
ans = 0
time = 0
for i in range(n):
  if time < w[i][0]:
    ans += 1
    time = w[i][1]

print(ans)