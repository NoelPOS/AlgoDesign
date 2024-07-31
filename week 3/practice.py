# coins = list(map(int, input().split()))
# change = int(input())

# def mincoin(v):

#  if v == 0:
#   return 0
#  if v < 0:
#   return float('inf')
#  else:
#   answer = float('inf')
#   for coin in coins:
#    diff = v - coin
#    result = 1 + mincoin(diff)
#    answer = min(answer, result)
#   return answer

# print(mincoin(change))


# prices = list(map(int, input().split()))

# def maxRev(l):
#  if l == 0:
#   return 0
#  if l < 0:
#   return float('-inf')
#  else:
#   max_rev = float('-inf')
#   for p in range(len(prices)):
#    diff = l - ( p + 1)
#    result = maxRev(diff) + prices[p]
#    max_rev = max(result, max_rev)

#   return max_rev
 
# print(maxRev(len(prices)))

# coins  = list(map(int, input().split()))
# change = int(input())

# memo = {}

# def minCoin(change):
#   if change in memo:
#     return memo[change]
#   if change == 0:
#     return 0
#   if change < 0:
#     return float('inf')
#   else:
#     mincoin = float('inf')
#     for c in coins:
#         temp = minCoin(change - c) + 1
#         mincoin = min(mincoin, temp)
#     memo[change] = mincoin
#     return mincoin
  
# print(minCoin(change))


# prices = list(map(int, input().split()))

# memo = {}

# def maxRev(l):
#   if l in memo:
#     return memo[l]
#   if l == 0:
#     return 0
#   if l < 0:
#     return float('-inf')
#   else:
#     max_rev = float('-inf')
#     for p in range(len(prices)):
#       diff = l - (p + 1)
#       result = maxRev(diff) + prices[p]
#       max_rev = max(max_rev, result)
#     memo[l] = max_rev
#     return max_rev
  
# print(maxRev(len(prices)))
import sys
sys.setrecursionlimit(100000)

prices = list(map(int, input().split()))
n = len(prices)

def maxRev(n):
  if n == 0:
    return 0
  else:
    max_rev = float('-inf')
    for i in range(1, n):
      if i <= n and prices[i - 1] != -1:
        remain = n - i
        max_rev = max(max_rev, prices[i - 1] + maxRev(remain))
        
    return max_rev

print(maxRev(n))





 



