import sys
sys.setrecursionlimit(10000)

user_in = int(input())
result = [0] * user_in

def comb(i):
 if i == user_in:
  print(result)
 else:
  result[i] = 0
  comb(i + 1)

  result[i] = 1
  comb(i + 1)

comb(0)


