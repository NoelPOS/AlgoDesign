import sys
sys.setrecursionlimit(10000)

N = int(input())
K = int(input())
result = [0] * N

def comb(i):
 if i == N:
  if result.count(1) == K:
   return 1
  else:
   return 0 
 else:
  result[i] = 0
  a = comb(i + 1)

  result[i] = 1
  b = comb(i + 1)
  return a + b

print(comb(0))