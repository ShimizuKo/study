L = int(input())
n = int(input())
x = list(map(int, input().split()))

ans_min = 0
ans_max = 0
for xi in x:
  ans_min = max(ans_min, min(xi, L - xi))
  ans_max = max(ans_max, xi, L - xi)
print(ans_min)
print(ans_max)