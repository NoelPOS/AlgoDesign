import sys
sys.setrecursionlimit(10000)

user_in = int(input())
K = int(input())
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

def fac(n):
 temp = 1
 while n > 0:
  temp *= n
  n -= 1
 return temp
 
num_com = comb(0)

k_com = fac(user_in) // (fac(user_in - K) * fac(K))

print("Total number of combinations", num_com)
print("Total number of combinations with excalty " + str(K) + "Ks is " , k_com )