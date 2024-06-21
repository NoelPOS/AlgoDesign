import sys
sys.setrecursionlimit(10000)

user_in = int(input())
result = [0] * user_in

def comb(i):
 if i == user_in:
  print(result)
  return 1
 else:
  result[i] = 0
  left = comb(i + 1)

  result[i] = 1
  right = comb(i+1)

  return left + right

print("Total number of combinations", comb(0))