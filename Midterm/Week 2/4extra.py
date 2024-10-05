import sys

sys.setrecursionlimit(10000)

N = int(input())
K = int(input())
result = [0] * N

def comb(i, s):
 if i == N:
  if s == K:
   return 1
  if N - i + s == K:
   return 0
  if N - i + s < K:
   return 0
  else:
   return 0
 
 result[i] = 0
 a = comb(i + 1, s)

 result[i] = 1
 b = comb(i + 1, s + 1)
 return a + b

print(comb(0, 0))