import sys
sys.setrecursionlimit(10000)

user_in = list(map(int, input().split()))

n = len(user_in)
result = [0] * n
min_diff = float('inf')

def comb(i):
 global min_diff
 if i == n:
  left = 0
  right = 0
  for j in range(len(user_in)):
   if result[j] == 0:
     left += user_in[j]
   else:
    right += user_in[j]
  diff = abs(left - right)
  if diff < min_diff:
   min_diff = diff

 else:
  result[i] = 0
  comb(i + 1)

  result[i] = 1
  comb(i + 1)


comb(0)

print(min_diff)