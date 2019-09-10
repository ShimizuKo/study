n = int(input())
a = list(map(int, input().split()))

a.sort(reverse = True)
ans = 0
for i in range(n - 2):
  if a[i] < a[i + 1] + a[i + 2]:
    ans = a[i] + a[i + 1] + a[i + 2]
    break
print(ans)