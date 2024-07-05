# K = int(input())
# k = int(input())

# X = [0] * K
# n = len(X)
# count = 0

# def comb(i , s):
#  global X
#  global count
#  if i == K:
#   if s == k:
#    return 1
#   elif n - i + s == k:
#    return 0
#   elif n - i + s < k:
#    return 0
#   else:
#    return 0 
#  else:
#   X[i] = 0
#   left = comb(i + 1, sum(X))
#   X[i] = 1
#   right =  comb(i + 1, sum(X))
#   return left + right

# print(comb(0, sum(X)))

     #               start
     #        (0, )         (1, )
     # (0, 0)     (0, 1)    (1, 0)   (1, 1) 


values = list(map(int, input().split()))
total = sum(values)
X = [0] * len(values)
min_diff = float('inf')

def minDiff(i, s):
 global min_diff
 if i == len(values):
  right = total - s
  min_diff = min(min_diff, abs(s - right)) 
 else:
  minDiff(i + 1,s + values[i] ) 
  minDiff(i + 1, s)
minDiff(0, 0)
print(min_diff)